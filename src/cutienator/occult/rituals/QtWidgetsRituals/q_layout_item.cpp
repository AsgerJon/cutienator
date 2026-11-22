//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QLayoutItem that Python can take functions over in. Every QLayoutItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQLayoutItemCall0)(const void *, int *);
typedef const QSize * (*CuteQLayoutItemCall1)(const void *, int *);
typedef const QSize * (*CuteQLayoutItemCall2)(const void *, int *);
typedef int (*CuteQLayoutItemCall3)(const void *, int *);
typedef void (*CuteQLayoutItemCall4)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQLayoutItemCall5)(const void *, int *);
typedef bool (*CuteQLayoutItemCall6)(const void *, int *);
typedef bool (*CuteQLayoutItemCall7)(const void *, int *);
typedef int (*CuteQLayoutItemCall8)(const void *, int, int *);
typedef int (*CuteQLayoutItemCall9)(const void *, int, int *);
typedef void (*CuteQLayoutItemCall10)(const void *, int *);
typedef void * (*CuteQLayoutItemCall11)(const void *, int *);
typedef void * (*CuteQLayoutItemCall12)(const void *, int *);
typedef void * (*CuteQLayoutItemCall13)(const void *, int *);
typedef int (*CuteQLayoutItemCall14)(const void *, int *);
class CuteQLayoutItem : public QLayoutItem {
public:
  using QLayoutItem::QLayoutItem;
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
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
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
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  QSize QLayoutItem::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLayoutItemCall0 call = reinterpret_cast<CuteQLayoutItemCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QSize QLayoutItem::minimumSize() const
  QSize minimumSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLayoutItemCall1 call = reinterpret_cast<CuteQLayoutItemCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QSize QLayoutItem::maximumSize() const
  QSize maximumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLayoutItemCall2 call = reinterpret_cast<CuteQLayoutItemCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  Qt::Orientations QLayoutItem::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLayoutItemCall3 call = reinterpret_cast<CuteQLayoutItemCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return {};
  }

  //  void QLayoutItem::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLayoutItemCall4 call = reinterpret_cast<CuteQLayoutItemCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }

  //  QRect QLayoutItem::geometry() const
  QRect geometry() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLayoutItemCall5 call = reinterpret_cast<CuteQLayoutItemCall5>(taken[5]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLayoutItemCall6 call = reinterpret_cast<CuteQLayoutItemCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QLayoutItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLayoutItemCall7 call = reinterpret_cast<CuteQLayoutItemCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLayoutItemCall8 call = reinterpret_cast<CuteQLayoutItemCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLayoutItemCall9 call = reinterpret_cast<CuteQLayoutItemCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  void QLayoutItem::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLayoutItemCall10 call = reinterpret_cast<CuteQLayoutItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QLayoutItem::invalidate();
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLayoutItemCall11 call = reinterpret_cast<CuteQLayoutItemCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QLayout *QLayoutItem::layout()
  QLayout *layout() override {
    if (taken[12]) {
      int handled = 0;
      CuteQLayoutItemCall12 call = reinterpret_cast<CuteQLayoutItemCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayoutItem::layout();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[13]) {
      int handled = 0;
      CuteQLayoutItemCall13 call = reinterpret_cast<CuteQLayoutItemCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }

  //  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQLayoutItemCall14 call = reinterpret_cast<CuteQLayoutItemCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayoutItem::controlTypes();
  }
};

//  QLayoutItem::~QLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItemD1Ev(QLayoutItem *self) {
  delete self;
}

//  QSize QLayoutItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem8sizeHintEv(const QLayoutItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLayoutItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem11minimumSizeEv(const QLayoutItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QLayoutItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem11maximumSizeEv(const QLayoutItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QLayoutItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem19expandingDirectionsEv(const QLayoutItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QLayoutItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem11setGeometryERK5QRect(
    QLayoutItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QLayoutItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QLayoutItem8geometryEv(const QLayoutItem *self) {
  return new QRect(self->geometry());
}

//  bool QLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLayoutItem7isEmptyEv(const QLayoutItem *self) {
  return self->isEmpty();
}

//  bool QLayoutItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLayoutItem17hasHeightForWidthEv(const QLayoutItem *self) {
  return self->hasHeightForWidth();
}

//  int QLayoutItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem14heightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QLayoutItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem21minimumHeightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  void QLayoutItem::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem10invalidateEv(QLayoutItem *self) {
  self->invalidate();
}

//  QWidget *QLayoutItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QLayoutItem6widgetEv(const QLayoutItem *self) {
  return self->widget();
}

//  QLayout *QLayoutItem::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN11QLayoutItem6layoutEv(QLayoutItem *self) {
  return self->layout();
}

//  QSpacerItem *QLayoutItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QLayoutItem10spacerItemEv(QLayoutItem *self) {
  return self->spacerItem();
}

//  Qt::Alignment QLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem9alignmentEv(const QLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLayoutItem::setAlignment(Qt::Alignment a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLayoutItem *self,
    int a) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a));
}

//  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem12controlTypesEv(const QLayoutItem *self) {
  return static_cast<int>(self->controlTypes().toInt());
}

//  a Python function taken by a CuteQLayoutItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLayoutItem(
    QLayoutItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLayoutItem *>(self)->take(key, call);
}

//  bool QLayoutItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QLayoutItem17hasHeightForWidthEv(
    const QLayoutItem *self) {
  return self->QLayoutItem::hasHeightForWidth();
}

//  int QLayoutItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QLayoutItem14heightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->QLayoutItem::heightForWidth(a0);
}

//  int QLayoutItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QLayoutItem21minimumHeightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->QLayoutItem::minimumHeightForWidth(a0);
}

//  void QLayoutItem::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLayoutItem10invalidateEv(QLayoutItem *self) {
  self->QLayoutItem::invalidate();
}

//  QWidget *QLayoutItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK11QLayoutItem6widgetEv(const QLayoutItem *self) {
  return self->QLayoutItem::widget();
}

//  QLayout *QLayoutItem::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN11QLayoutItem6layoutEv(QLayoutItem *self) {
  return self->QLayoutItem::layout();
}

//  QSpacerItem *QLayoutItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_own_ZN11QLayoutItem10spacerItemEv(QLayoutItem *self) {
  return self->QLayoutItem::spacerItem();
}

//  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QLayoutItem12controlTypesEv(const QLayoutItem *self) {
  return static_cast<int>(self->QLayoutItem::controlTypes().toInt());
}
