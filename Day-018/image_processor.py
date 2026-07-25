# Simulate Parallel Image Processing

from multiprocessing import Pool
import time
import random


def process_image(image):

    processing_time = random.randint(2, 5)

    time.sleep(processing_time)

    return f"{image} processed in {processing_time} seconds"


if __name__ == "__main__":

    images = [

        "image1.jpg",

        "image2.jpg",

        "image3.jpg",

        "image4.jpg",

        "image5.jpg"

    ]

    start = time.perf_counter()

    with Pool() as pool:

        results = pool.map(process_image, images)

    end = time.perf_counter()

    print("\nProcessing Results\n")

    for result in results:
        print(result)

    print(f"\nTotal Processing Time = {end-start:.2f} seconds")
