from analyzer import Analyzer


def main():
    analyzer = Analyzer("imgs/15375435888520.jpg", "imgs/")
    imgs = analyzer.detect()
    analyzer.create_html(imgs)


if __name__ == "__main__":
    main()
