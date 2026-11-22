//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QWidgetItemV2 that Python can take functions over in. Every QWidgetItemV2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQWidgetItemV2Call0)(const void *, int *);
typedef const QSize * (*CuteQWidgetItemV2Call1)(const void *, int *);
typedef const QSize * (*CuteQWidgetItemV2Call2)(const void *, int *);
typedef int (*CuteQWidgetItemV2Call3)(const void *, int, int *);
typedef bool (*CuteQWidgetItemV2Call4)(const void *, int *);
typedef void (*CuteQWidgetItemV2Call5)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQWidgetItemV2Call6)(const void *, int *);
typedef void * (*CuteQWidgetItemV2Call7)(const void *, int *);
typedef bool (*CuteQWidgetItemV2Call8)(const void *, int *);
typedef int (*CuteQWidgetItemV2Call9)(const void *, int, int *);
typedef void (*CuteQWidgetItemV2Call10)(const void *, int *);
typedef void * (*CuteQWidgetItemV2Call11)(const void *, int *);
typedef void * (*CuteQWidgetItemV2Call12)(const void *, int *);
class CuteQWidgetItemV2 : public QWidgetItemV2 {
public:
  using QWidgetItemV2::QWidgetItemV2;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  QSize QWidgetItemV2::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetItemV2Call0 call = reinterpret_cast<CuteQWidgetItemV2Call0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItemV2::sizeHint();
  }

  //  QSize QWidgetItemV2::minimumSize() const
  QSize minimumSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetItemV2Call1 call = reinterpret_cast<CuteQWidgetItemV2Call1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItemV2::minimumSize();
  }

  //  QSize QWidgetItemV2::maximumSize() const
  QSize maximumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetItemV2Call2 call = reinterpret_cast<CuteQWidgetItemV2Call2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItemV2::maximumSize();
  }

  //  int QWidgetItemV2::heightForWidth(int width) const
  int heightForWidth(int width) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetItemV2Call3 call = reinterpret_cast<CuteQWidgetItemV2Call3>(taken[3]);
      int given = call(this, width, &handled);
      if (handled) return given;
    }
    return QWidgetItemV2::heightForWidth(width);
  }

  //  bool QWidgetItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetItemV2Call4 call = reinterpret_cast<CuteQWidgetItemV2Call4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetItem::isEmpty();
  }

  //  void QWidgetItem::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetItemV2Call5 call = reinterpret_cast<CuteQWidgetItemV2Call5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QWidgetItem::setGeometry(a0);
  }

  //  QRect QWidgetItem::geometry() const
  QRect geometry() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetItemV2Call6 call = reinterpret_cast<CuteQWidgetItemV2Call6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::geometry();
  }

  //  QWidget *QWidgetItem::widget() const
  QWidget *widget() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetItemV2Call7 call = reinterpret_cast<CuteQWidgetItemV2Call7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QWidgetItem::widget();
  }

  //  bool QWidgetItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetItemV2Call8 call = reinterpret_cast<CuteQWidgetItemV2Call8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetItem::hasHeightForWidth();
  }

  //  int QWidgetItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetItemV2Call9 call = reinterpret_cast<CuteQWidgetItemV2Call9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetItem::minimumHeightForWidth(a0);
  }

  //  void QLayoutItem::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetItemV2Call10 call = reinterpret_cast<CuteQWidgetItemV2Call10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QLayoutItem::invalidate();
  }

  //  QLayout *QLayoutItem::layout()
  QLayout *layout() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWidgetItemV2Call11 call = reinterpret_cast<CuteQWidgetItemV2Call11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayoutItem::layout();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[12]) {
      int handled = 0;
      CuteQWidgetItemV2Call12 call = reinterpret_cast<CuteQWidgetItemV2Call12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  QWidgetItemV2::QWidgetItemV2(QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidgetItemV2 *ritual_ZN13QWidgetItemV2C1EP7QWidget(QWidget *widget) {
  return new CuteQWidgetItemV2(widget);
}

//  QWidgetItemV2::~QWidgetItemV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetItemV2D1Ev(QWidgetItemV2 *self) {
  delete self;
}

//  QSize QWidgetItemV2::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV28sizeHintEv(const QWidgetItemV2 *self) {
  return new QSize(self->sizeHint());
}

//  QSize QWidgetItemV2::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV211minimumSizeEv(const QWidgetItemV2 *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWidgetItemV2::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV211maximumSizeEv(const QWidgetItemV2 *self) {
  return new QSize(self->maximumSize());
}

//  int QWidgetItemV2::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QWidgetItemV214heightForWidthEi(
    const QWidgetItemV2 *self,
    int width) {
  return self->heightForWidth(width);
}

//  a Python function taken by a CuteQWidgetItemV2, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetItemV2(
    QWidgetItemV2 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetItemV2 *>(self)->take(key, call);
}

//  QSize QWidgetItemV2::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QWidgetItemV28sizeHintEv(const QWidgetItemV2 *self) {
  return new QSize(self->QWidgetItemV2::sizeHint());
}

//  QSize QWidgetItemV2::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QWidgetItemV211minimumSizeEv(
    const QWidgetItemV2 *self) {
  return new QSize(self->QWidgetItemV2::minimumSize());
}

//  QSize QWidgetItemV2::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QWidgetItemV211maximumSizeEv(
    const QWidgetItemV2 *self) {
  return new QSize(self->QWidgetItemV2::maximumSize());
}

//  int QWidgetItemV2::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QWidgetItemV214heightForWidthEi(
    const QWidgetItemV2 *self,
    int width) {
  return self->QWidgetItemV2::heightForWidth(width);
}
