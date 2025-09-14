import cv2
import numpy as np

# ----------------------------
# Helper: Convert BGR to basic color name
# ----------------------------
def get_color_name(b, g, r):
    # Define some common colors (BGR format)
    colors = {
        "Red": (0, 0, 255),
        "Green": (0, 255, 0),
        "Blue": (255, 0, 0),
        "Yellow": (0, 255, 255),
        "Orange": (0, 165, 255),
        "Purple": (128, 0, 128),
        "White": (255, 255, 255),
        "Black": (0, 0, 0),
        "Gray": (128, 128, 128)
    }

    # Find the closest color by Euclidean distance
    min_dist = float("inf")
    color_name = "Unknown"
    for name, (cb, cg, cr) in colors.items():
        dist = np.sqrt((b - cb) ** 2 + (g - cg) ** 2 + (r - cr) ** 2)
        if dist < min_dist:
            min_dist = dist
            color_name = name
    return color_name


# ----------------------------
# Main Program
# ----------------------------
def detect_box_color(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image. Check path.")
        return

    # Resize for easier processing
    image = cv2.resize(image, (400, 400))

    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # For simplicity: Assume the box is in the center of the image
    h, w, _ = image.shape
    box_region = hsv[h//4:h*3//4, w//4:w*3//4]  # central region

    # Find average color in that region
    avg_color = cv2.mean(box_region)[:3]  # (H, S, V)
    avg_bgr = cv2.mean(image[h//4:h*3//4, w//4:w*3//4])[:3]  # (B, G, R)

    # Convert to integer
    avg_bgr = tuple(map(int, avg_bgr))

    # Get nearest color name
    color_name = get_color_name(*avg_bgr)

    # Show results
    print(f"Detected Box Color: {color_name}")
    print(f"Average BGR Value: {avg_bgr}")

    # Draw rectangle for visualization
    output = image.copy()
    cv2.rectangle(output, (w//4, h//4), (w*3//4, h*3//4), (0, 0, 0), 2)
    cv2.putText(output, color_name, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Detected Box", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ----------------------------
# Run the function
# ----------------------------
if __name__ == "__main__":
    detect_box_color("box.png")  # change to your image path
