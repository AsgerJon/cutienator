//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/layoutdecoration.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/layoutdecoration.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerLayoutDecorationExtension that Python can take functions over in. Every QDesignerLayoutDecorationExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRect * (*CuteQDesignerLayoutDecorationExtensionCall0)(const void *, int, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall1)(const void *, QWidget *, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall2)(const void *, QLayoutItem *, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall3)(const void *, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall4)(const void *, int *);
typedef void (*CuteQDesignerLayoutDecorationExtensionCall5)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerLayoutDecorationExtensionCall6)(const void *, int, int *);
typedef void (*CuteQDesignerLayoutDecorationExtensionCall7)(const void *, int, int *);
typedef void (*CuteQDesignerLayoutDecorationExtensionCall8)(const void *, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall9)(const void *, const QPoint *, int *);
typedef int (*CuteQDesignerLayoutDecorationExtensionCall10)(const void *, int, int, int *);
typedef void (*CuteQDesignerLayoutDecorationExtensionCall11)(const void *, const QPoint *, int, int *);
class CuteQDesignerLayoutDecorationExtension : public QDesignerLayoutDecorationExtension {
public:
  using QDesignerLayoutDecorationExtension::QDesignerLayoutDecorationExtension;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension8itemInfoEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension7indexOfEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension7indexOfEP11QLayoutItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension17currentInsertModeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension12currentIndexEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension12removeWidgetEP7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension9insertRowEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension12insertColumnEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension8simplifyEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension10findItemAtERK6QPoint")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension10findItemAtEii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension15adjustIndicatorERK6QPointi")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QRect QDesignerLayoutDecorationExtension::itemInfo(int index) const
  QRect itemInfo(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall0 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall0>(taken[0]);
      const QRect * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QDesignerLayoutDecorationExtension::indexOf(QWidget *widget)
  //      const
  int indexOf(QWidget *widget) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall1 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall1>(taken[1]);
      int given = call(this, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerLayoutDecorationExtension::indexOf(QLayoutItem *item)
  //      const
  int indexOf(QLayoutItem *item) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall2 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall2>(taken[2]);
      int given = call(this, item, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  InsertMode QDesignerLayoutDecorationExtension::currentInsertMode()
  //      const
  QDesignerLayoutDecorationExtension::InsertMode currentInsertMode() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall3 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerLayoutDecorationExtension::InsertMode>(given);
    }
    return {};
  }

  //  int QDesignerLayoutDecorationExtension::currentIndex() const
  int currentIndex() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall4 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerLayoutDecorationExtension::removeWidget(QWidget
  //      *widget)
  void removeWidget(QWidget *widget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall5 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall5>(taken[5]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::insertRow(int row)
  void insertRow(int row) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall6 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall6>(taken[6]);
      call(this, row, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::insertColumn(int column)
  void insertColumn(int column) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall7 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall7>(taken[7]);
      call(this, column, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::simplify()
  void simplify() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall8 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  int QDesignerLayoutDecorationExtension::findItemAt(const QPoint &pos)
  //      const
  int findItemAt(const QPoint &pos) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall9 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall9>(taken[9]);
      int given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerLayoutDecorationExtension::findItemAt(int row, int
  //      column) const
  int findItemAt(int row, int column) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall10 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall10>(taken[10]);
      int given = call(this, row, column, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerLayoutDecorationExtension::adjustIndicator(const QPoint
  //      &pos, int index)
  void adjustIndicator(const QPoint &pos, int index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerLayoutDecorationExtensionCall11 call = reinterpret_cast<CuteQDesignerLayoutDecorationExtensionCall11>(taken[11]);
      call(this, &pos, index, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerLayoutDecorationExtension::~QDesignerLayoutDecorationExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtensionD1Ev(
    QDesignerLayoutDecorationExtension *self) {
  delete self;
}

//  QList<QWidget *> QDesignerLayoutDecorationExtension::widgets(QLayout
//      *layout) const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK34QDesignerLayoutDecorationExtension7widgetsEP7QLayout(
    const QDesignerLayoutDecorationExtension *self,
    QLayout *layout) {
  return new QList<QWidget *>(self->widgets(layout));
}

//  QRect QDesignerLayoutDecorationExtension::itemInfo(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK34QDesignerLayoutDecorationExtension8itemInfoEi(
    const QDesignerLayoutDecorationExtension *self,
    int index) {
  return new QRect(self->itemInfo(index));
}

//  int QDesignerLayoutDecorationExtension::indexOf(QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerLayoutDecorationExtension7indexOfEP7QWidget(
    const QDesignerLayoutDecorationExtension *self,
    QWidget *widget) {
  return self->indexOf(widget);
}

//  int QDesignerLayoutDecorationExtension::indexOf(QLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerLayoutDecorationExtension7indexOfEP11QLayoutItem(
    const QDesignerLayoutDecorationExtension *self,
    QLayoutItem *item) {
  return self->indexOf(item);
}

//  InsertMode QDesignerLayoutDecorationExtension::currentInsertMode() const
extern "C" Q_DECL_EXPORT
QDesignerLayoutDecorationExtension::InsertMode ritual_ZNK34QDesignerLayoutDecorationExtension17currentInsertModeEv(
    const QDesignerLayoutDecorationExtension *self) {
  return self->currentInsertMode();
}

//  int QDesignerLayoutDecorationExtension::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerLayoutDecorationExtension12currentIndexEv(
    const QDesignerLayoutDecorationExtension *self) {
  return self->currentIndex();
}

//  void QDesignerLayoutDecorationExtension::removeWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtension12removeWidgetEP7QWidget(
    QDesignerLayoutDecorationExtension *self,
    QWidget *widget) {
  self->removeWidget(widget);
}

//  void QDesignerLayoutDecorationExtension::insertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtension9insertRowEi(
    QDesignerLayoutDecorationExtension *self,
    int row) {
  self->insertRow(row);
}

//  void QDesignerLayoutDecorationExtension::insertColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtension12insertColumnEi(
    QDesignerLayoutDecorationExtension *self,
    int column) {
  self->insertColumn(column);
}

//  void QDesignerLayoutDecorationExtension::simplify()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtension8simplifyEv(
    QDesignerLayoutDecorationExtension *self) {
  self->simplify();
}

//  int QDesignerLayoutDecorationExtension::findItemAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerLayoutDecorationExtension10findItemAtERK6QPoint(
    const QDesignerLayoutDecorationExtension *self,
    const QPoint *pos) {
  return self->findItemAt(*pos);
}

//  int QDesignerLayoutDecorationExtension::findItemAt(int row, int column)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerLayoutDecorationExtension10findItemAtEii(
    const QDesignerLayoutDecorationExtension *self,
    int row,
    int column) {
  return self->findItemAt(row, column);
}

//  void QDesignerLayoutDecorationExtension::adjustIndicator(const QPoint
//      &pos, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerLayoutDecorationExtension15adjustIndicatorERK6QPointi(
    QDesignerLayoutDecorationExtension *self,
    const QPoint *pos,
    int index) {
  self->adjustIndicator(*pos, index);
}

//  a Python function taken by a CuteQDesignerLayoutDecorationExtension, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerLayoutDecorationExtension(
    QDesignerLayoutDecorationExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerLayoutDecorationExtension *>(self)->take(key, call);
}
