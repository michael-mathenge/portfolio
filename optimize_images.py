from PIL import Image
import os

def optimize_image(input_path, output_path, quality=85, max_size=(1920, 1080)):
    with Image.open(input_path) as img:
        # Resize if larger than max_size
        img.thumbnail(max_size, Image.LANCZOS)
        
        # Convert to WebP
        output_webp = os.path.splitext(output_path)[0] + '.webp'
        img.save(output_webp, 'WEBP', quality=quality)
        print(f"Optimized {input_path} -> {output_webp}")

def optimize_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                
                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Always convert, even if file exists
                optimize_image(input_path, output_path)
                
                # Print for verification
                print(f'Processed: {input_path} -> {output_path}')

if __name__ == '__main__':
    # Define specific directories to optimize
    directories = [
        ('static/assets/img', 'static/assets/img_optimized'),
        ('static/assets/img/masonry-portfolio', 'static/assets/img_optimized/masonry-portfolio'),
        ('static/assets/img/testimonials', 'static/assets/img_optimized/testimonials'),
        ('static/assets/img/portfolio', 'static/assets/img_optimized/portfolio')
    ]
    
    # Optimize each directory
    for input_dir, output_dir in directories:
        optimize_directory(input_dir, output_dir)
