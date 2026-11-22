//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QWidgetItem that Python can take functions over in. Every QWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQWidgetItemCall0)(const void *, int *);
typedef const QSize * (*CuteQWidgetItemCall1)(const void *, int *);
typedef const QSize * (*CuteQWidgetItemCall2)(const void *, int *);
typedef bool (*CuteQWidgetItemCall3)(const void *, int *);
typedef void (*CuteQWidgetItemCall4)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQWidgetItemCall5)(const void *, int *);
typedef void * (*CuteQWidgetItemCall6)(const void *, int *);
typedef bool (*CuteQWidgetItemCall7)(const void *, int *);
typedef int (*CuteQWidgetItemCall8)(const void *, int, int *);
typedef int (*CuteQWidgetItemCall9)(const void *, int, int *);
typedef void (*CuteQWidgetItemCall10)(const void *, int *);
typedef void * (*CuteQWidgetItemCall11)(const void *, int *);
typedef void * (*CuteQWidgetItemCall12)(const void *, int *);
class CuteQWidgetItem : public QWidgetItem {
public:
  using QWidgetItem::QWidgetItem;
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
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
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

  //  QSize QWidgetItem::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetItemCall0 call = reinterpret_cast<CuteQWidgetItemCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::sizeHint();
  }

  //  QSize QWidgetItem::minimumSize() const
  QSize minimumSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetItemCall1 call = reinterpret_cast<CuteQWidgetItemCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::minimumSize();
  }

  //  QSize QWidgetItem::maximumSize() const
  QSize maximumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetItemCall2 call = reinterpret_cast<CuteQWidgetItemCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::maximumSize();
  }

  //  bool QWidgetItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetItemCall3 call = reinterpret_cast<CuteQWidgetItemCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetItem::isEmpty();
  }

  //  void QWidgetItem::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetItemCall4 call = reinterpret_cast<CuteQWidgetItemCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QWidgetItem::setGeometry(a0);
  }

  //  QRect QWidgetItem::geometry() const
  QRect geometry() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetItemCall5 call = reinterpret_cast<CuteQWidgetItemCall5>(taken[5]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::geometry();
  }

  //  QWidget *QWidgetItem::widget() const
  QWidget *widget() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetItemCall6 call = reinterpret_cast<CuteQWidgetItemCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QWidgetItem::widget();
  }

  //  bool QWidgetItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetItemCall7 call = reinterpret_cast<CuteQWidgetItemCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetItem::hasHeightForWidth();
  }

  //  int QWidgetItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetItemCall8 call = reinterpret_cast<CuteQWidgetItemCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetItem::heightForWidth(a0);
  }

  //  int QWidgetItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetItemCall9 call = reinterpret_cast<CuteQWidgetItemCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetItem::minimumHeightForWidth(a0);
  }

  //  void QLayoutItem::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetItemCall10 call = reinterpret_cast<CuteQWidgetItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QLayoutItem::invalidate();
  }

  //  QLayout *QLayoutItem::layout()
  QLayout *layout() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWidgetItemCall11 call = reinterpret_cast<CuteQWidgetItemCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayoutItem::layout();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[12]) {
      int handled = 0;
      CuteQWidgetItemCall12 call = reinterpret_cast<CuteQWidgetItemCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  QWidgetItem::QWidgetItem(QWidget *w)
extern "C" Q_DECL_EXPORT
QWidgetItem *ritual_ZN11QWidgetItemC1EP7QWidget(QWidget *w) {
  return new CuteQWidgetItem(w);
}

//  QWidgetItem::~QWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWidgetItemD1Ev(QWidgetItem *self) {
  delete self;
}

//  QSize QWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem8sizeHintEv(const QWidgetItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem11minimumSizeEv(const QWidgetItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWidgetItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem11maximumSizeEv(const QWidgetItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QWidgetItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem19expandingDirectionsEv(const QWidgetItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  bool QWidgetItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWidgetItem7isEmptyEv(const QWidgetItem *self) {
  return self->isEmpty();
}

//  void QWidgetItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWidgetItem11setGeometryERK5QRect(
    QWidgetItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QWidgetItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QWidgetItem8geometryEv(const QWidgetItem *self) {
  return new QRect(self->geometry());
}

//  QWidget *QWidgetItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QWidgetItem6widgetEv(const QWidgetItem *self) {
  return self->widget();
}

//  bool QWidgetItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWidgetItem17hasHeightForWidthEv(const QWidgetItem *self) {
  return self->hasHeightForWidth();
}

//  int QWidgetItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem14heightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QWidgetItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem21minimumHeightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  QSizePolicy::ControlTypes QWidgetItem::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem12controlTypesEv(const QWidgetItem *self) {
  return static_cast<int>(self->controlTypes().toInt());
}

//  a Python function taken by a CuteQWidgetItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetItem(
    QWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetItem *>(self)->take(key, call);
}

//  QSize QWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QWidgetItem8sizeHintEv(const QWidgetItem *self) {
  return new QSize(self->QWidgetItem::sizeHint());
}

//  QSize QWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QWidgetItem11minimumSizeEv(const QWidgetItem *self) {
  return new QSize(self->QWidgetItem::minimumSize());
}

//  QSize QWidgetItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QWidgetItem11maximumSizeEv(const QWidgetItem *self) {
  return new QSize(self->QWidgetItem::maximumSize());
}

//  bool QWidgetItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWidgetItem7isEmptyEv(const QWidgetItem *self) {
  return self->QWidgetItem::isEmpty();
}

//  void QWidgetItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QWidgetItem11setGeometryERK5QRect(
    QWidgetItem *self,
    const QRect *a0) {
  self->QWidgetItem::setGeometry(*a0);
}

//  QRect QWidgetItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QWidgetItem8geometryEv(const QWidgetItem *self) {
  return new QRect(self->QWidgetItem::geometry());
}

//  QWidget *QWidgetItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK11QWidgetItem6widgetEv(const QWidgetItem *self) {
  return self->QWidgetItem::widget();
}

//  bool QWidgetItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWidgetItem17hasHeightForWidthEv(
    const QWidgetItem *self) {
  return self->QWidgetItem::hasHeightForWidth();
}

//  int QWidgetItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QWidgetItem14heightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->QWidgetItem::heightForWidth(a0);
}

//  int QWidgetItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QWidgetItem21minimumHeightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->QWidgetItem::minimumHeightForWidth(a0);
}
