from PIL import Image, ImageDraw

from Tupper.tupper_constants import IMAGE_MODE, WIDTH, HEIGHT, \
    AREA, SIZE_TUPLE, DEFAULT_IMAGE_COLOR

class TupperDecoder:
    def _height_to_bin(self, height: int) -> str:
        
        height //= 17

        bin_tail = bin(height)[2:]
        remain = (AREA - len(bin_tail))
        binary = ('0' * remain) + bin_tail

        return binary

    def _bin_to_image_lists(self, binary: str) -> list:
        
        image_lists = [list() for x in range(HEIGHT)]

        for i in range(AREA):
            current_row = -(i % HEIGHT)
            image_lists[current_row].append(binary[i])

        return image_lists
    

    def generate_image(self, height: int) -> Image:
        
        binary = self._height_to_bin(height)
        image_lists = self._bin_to_image_lists(binary)

        image = Image.new(
            IMAGE_MODE, 
            SIZE_TUPLE, 
            DEFAULT_IMAGE_COLOR
        )

        for y in range(HEIGHT):
            for x in range(WIDTH):
                pixel_value = (int(image_lists[y][x],))

                image.putpixel(
                    xy=(WIDTH - x - 1, -y),
                    value=pixel_value
                )

        return image
