from src.model.annotator import Annotator
from src.controller.annotator import AnnotatorController
from src.view.annotator import AnnotatorView


def main():
    model = Annotator.create()
    ctrl = AnnotatorController()
    view = AnnotatorView()

    model.add_view(view)
    ctrl.model = model
    view.ctrl = ctrl

    view.annotator_view()


if __name__ == '__main__':
    main()
