//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qsizepolicy.h>
#include <cstring>

//  A QSpacerItem that Python can take functions over in. Every QSpacerItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSpacerItemCall0)(const void *, int *);
typedef const QSize * (*CuteQSpacerItemCall1)(const void *, int *);
typedef const QSize * (*CuteQSpacerItemCall2)(const void *, int *);
typedef int (*CuteQSpacerItemCall3)(const void *, int *);
typedef bool (*CuteQSpacerItemCall4)(const void *, int *);
typedef void (*CuteQSpacerItemCall5)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQSpacerItemCall6)(const void *, int *);
typedef void * (*CuteQSpacerItemCall7)(const void *, int *);
typedef bool (*CuteQSpacerItemCall8)(const void *, int *);
typedef int (*CuteQSpacerItemCall9)(const void *, int, int *);
typedef int (*CuteQSpacerItemCall10)(const void *, int, int *);
typedef void (*CuteQSpacerItemCall11)(const void *, int *);
typedef void * (*CuteQSpacerItemCall12)(const void *, int *);
typedef void * (*CuteQSpacerItemCall13)(const void *, int *);
typedef int (*CuteQSpacerItemCall14)(const void *, int *);
class CuteQSpacerItem : public QSpacerItem {
public:
  using QSpacerItem::QSpacerItem;
  CuteQSpacerItem(const QSpacerItem &other) : QSpacerItem(other) {}
  void *taken[15] = {};

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
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
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
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  QSize QSpacerItem::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpacerItemCall0 call = reinterpret_cast<CuteQSpacerItemCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSpacerItem::sizeHint();
  }

  //  QSize QSpacerItem::minimumSize() const
  QSize minimumSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpacerItemCall1 call = reinterpret_cast<CuteQSpacerItemCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSpacerItem::minimumSize();
  }

  //  QSize QSpacerItem::maximumSize() const
  QSize maximumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpacerItemCall2 call = reinterpret_cast<CuteQSpacerItemCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSpacerItem::maximumSize();
  }

  //  Qt::Orientations QSpacerItem::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpacerItemCall3 call = reinterpret_cast<CuteQSpacerItemCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QSpacerItem::expandingDirections();
  }

  //  bool QSpacerItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSpacerItemCall4 call = reinterpret_cast<CuteQSpacerItemCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSpacerItem::isEmpty();
  }

  //  void QSpacerItem::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSpacerItemCall5 call = reinterpret_cast<CuteQSpacerItemCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSpacerItem::setGeometry(a0);
  }

  //  QRect QSpacerItem::geometry() const
  QRect geometry() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSpacerItemCall6 call = reinterpret_cast<CuteQSpacerItemCall6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSpacerItem::geometry();
  }

  //  QSpacerItem *QSpacerItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSpacerItemCall7 call = reinterpret_cast<CuteQSpacerItemCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QSpacerItem::spacerItem();
  }

  //  bool QLayoutItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSpacerItemCall8 call = reinterpret_cast<CuteQSpacerItemCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSpacerItemCall9 call = reinterpret_cast<CuteQSpacerItemCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSpacerItemCall10 call = reinterpret_cast<CuteQSpacerItemCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  void QLayoutItem::invalidate()
  void invalidate() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSpacerItemCall11 call = reinterpret_cast<CuteQSpacerItemCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QLayoutItem::invalidate();
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSpacerItemCall12 call = reinterpret_cast<CuteQSpacerItemCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QLayout *QLayoutItem::layout()
  QLayout *layout() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSpacerItemCall13 call = reinterpret_cast<CuteQSpacerItemCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayoutItem::layout();
  }

  //  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSpacerItemCall14 call = reinterpret_cast<CuteQSpacerItemCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayoutItem::controlTypes();
  }
};

//  QSpacerItem::QSpacerItem(int w, int h, QSizePolicy::Policy hData,
//      QSizePolicy::Policy vData)
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QSpacerItemC1EiiN11QSizePolicy6PolicyES1_(
    int w,
    int h,
    QSizePolicy::Policy hData,
    QSizePolicy::Policy vData) {
  return new CuteQSpacerItem(w, h, hData, vData);
}

//  QSpacerItem::~QSpacerItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItemD1Ev(QSpacerItem *self) {
  delete self;
}

//  void QSpacerItem::changeSize(int w, int h, QSizePolicy::Policy hData,
//      QSizePolicy::Policy vData)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItem10changeSizeEiiN11QSizePolicy6PolicyES1_(
    QSpacerItem *self,
    int w,
    int h,
    QSizePolicy::Policy hData,
    QSizePolicy::Policy vData) {
  self->changeSize(w, h, hData, vData);
}

//  QSize QSpacerItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem8sizeHintEv(const QSpacerItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSpacerItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem11minimumSizeEv(const QSpacerItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QSpacerItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem11maximumSizeEv(const QSpacerItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QSpacerItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSpacerItem19expandingDirectionsEv(const QSpacerItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  bool QSpacerItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSpacerItem7isEmptyEv(const QSpacerItem *self) {
  return self->isEmpty();
}

//  void QSpacerItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItem11setGeometryERK5QRect(
    QSpacerItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QSpacerItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QSpacerItem8geometryEv(const QSpacerItem *self) {
  return new QRect(self->geometry());
}

//  QSpacerItem *QSpacerItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QSpacerItem10spacerItemEv(QSpacerItem *self) {
  return self->spacerItem();
}

//  QSizePolicy QSpacerItem::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZNK11QSpacerItem10sizePolicyEv(const QSpacerItem *self) {
  return new QSizePolicy(self->sizePolicy());
}

//  a Python function taken by a CuteQSpacerItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpacerItem(
    QSpacerItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpacerItem *>(self)->take(key, call);
}

//  QSize QSpacerItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QSpacerItem8sizeHintEv(const QSpacerItem *self) {
  return new QSize(self->QSpacerItem::sizeHint());
}

//  QSize QSpacerItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QSpacerItem11minimumSizeEv(const QSpacerItem *self) {
  return new QSize(self->QSpacerItem::minimumSize());
}

//  QSize QSpacerItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QSpacerItem11maximumSizeEv(const QSpacerItem *self) {
  return new QSize(self->QSpacerItem::maximumSize());
}

//  Qt::Orientations QSpacerItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QSpacerItem19expandingDirectionsEv(
    const QSpacerItem *self) {
  return static_cast<int>(self->QSpacerItem::expandingDirections().toInt());
}

//  bool QSpacerItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSpacerItem7isEmptyEv(const QSpacerItem *self) {
  return self->QSpacerItem::isEmpty();
}

//  void QSpacerItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSpacerItem11setGeometryERK5QRect(
    QSpacerItem *self,
    const QRect *a0) {
  self->QSpacerItem::setGeometry(*a0);
}

//  QRect QSpacerItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QSpacerItem8geometryEv(const QSpacerItem *self) {
  return new QRect(self->QSpacerItem::geometry());
}

//  QSpacerItem *QSpacerItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_own_ZN11QSpacerItem10spacerItemEv(QSpacerItem *self) {
  return self->QSpacerItem::spacerItem();
}
