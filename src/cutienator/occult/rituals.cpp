#include <QtCore/QPoint>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

static int argc = 1;
static char name[] = "cutienator";
static char *argv[] = {name, nullptr};

extern "C" int add(int a, int b) {
  return a + b;
}

extern "C" int manhattan(int x, int y) {
  return QPoint(x, y).manhattanLength();
}

extern "C" QApplication *newApplication() {
  return new QApplication(argc, argv);
}

extern "C" QWidget *newWidget() {
  return new QWidget();
}

extern "C" void showWidget(QWidget *widget) {
  widget->show();
}

extern "C" int runApplication() {
  return QApplication::exec();
}
