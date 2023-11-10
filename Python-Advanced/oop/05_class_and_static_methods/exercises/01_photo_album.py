from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(self.pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def __init_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    def add_photo(self, label):
        for page, photo_line in enumerate(self.photos):
            if len(photo_line) < PhotoAlbum.PHOTOS_PER_PAGE:
                photo_line.append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(photo_line)}"
        return "No more free slots"

    def display(self):
        page_sep = '-' * 11
        result = [page_sep]
        for page_line in self.photos:
            result.append(' '.join(['[]' for _ in page_line]))
            result.append(page_sep)
        return '\n'.join(result)


# a = [[[]] * 3] * 4
# print('-----------')
# for page in a:
#     for photo in page:
#         if photo
#         print(photo, end=' ')
#     print()
#     print('-----------')