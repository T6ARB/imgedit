import click
from PIL import Image, ImageDraw, ImageFont
import os

@click.group()
def cli():
    """Simple Image Editor CLI"""
    pass

@cli.command()
@click.option('--input', '-i', required=True, help='Path to the input image')
@click.option('--output', '-o', required=True, help='Path to save the edited image')
@click.option('--width', type=int, help='New width of the image')
@click.option('--height', type=int, help='New height of the image')
def resize(input, output, width, height):
    """Resize the image to specified width and height"""
    img = Image.open(input)
    new_size = (width if width else img.width, height if height else img.height)
    img = img.resize(new_size)
    img.save(output)
    click.echo(f'✅ Resized image to {new_size} and saved to {output}')

@cli.command()
@click.option('--input', '-i', required=True, help='Path to the input image')
@click.option('--output', '-o', required=True, help='Path to save the edited image')
@click.option('--angle', type=float, required=True, help='Rotation angle in degrees')
def rotate(input, output, angle):
    """Rotate the image by given angle"""
    img = Image.open(input)
    img = img.rotate(angle, expand=True)
    img.save(output)
    click.echo(f'✅ Rotated image by {angle} degrees and saved to {output}')

@cli.command()
@click.option('--input', '-i', required=True, help='Path to the input image')
@click.option('--output', '-o', required=True, help='Path to save the edited image')
@click.option('--text', '-t', required=True, help='Text to add on the image')
@click.option('--x', type=int, default=10, help='X coordinate for the text position')
@click.option('--y', type=int, default=10, help='Y coordinate for the text position')
def add_text(input, output, text, x, y):
    """Add text to the image at specified position"""
    img = Image.open(input)
    draw = ImageDraw.Draw(img)
    font_path = os.path.join('fonts', 'Arial.ttf')
    font = ImageFont.truetype(font_path, 24)
    draw.text((x, y), text, fill='white', font=font)
    img.save(output)
    click.echo(f'✅ Added text "{text}" at position ({x}, {y}) and saved to {output}')

@cli.command()
@click.option('--input', '-i', required=True, help='Path to the input image')
@click.option('--output', '-o', required=True, help='Path to save the edited image')
def bw(input, output):
    """Convert image to black and white (grayscale)"""
    img = Image.open(input)
    img = img.convert('L')
    img.save(output)
    click.echo(f'✅ Converted image to black & white and saved to {output}')

if __name__ == '__main__':
    cli()
