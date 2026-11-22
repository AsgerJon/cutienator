//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstackedlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstackedlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QStackedLayout that Python can take functions over in. Every QStackedLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQStackedLayoutCall0)(const void *, int *);
typedef void (*CuteQStackedLayoutCall1)(const void *, QLayoutItem *, int *);
typedef const QSize * (*CuteQStackedLayoutCall2)(const void *, int *);
typedef const QSize * (*CuteQStackedLayoutCall3)(const void *, int *);
typedef void * (*CuteQStackedLayoutCall4)(const void *, int, int *);
typedef void * (*CuteQStackedLayoutCall5)(const void *, int, int *);
typedef void (*CuteQStackedLayoutCall6)(const void *, const QRect *, int *);
typedef bool (*CuteQStackedLayoutCall7)(const void *, int *);
typedef int (*CuteQStackedLayoutCall8)(const void *, int, int *);
typedef int (*CuteQStackedLayoutCall9)(const void *, int *);
typedef void (*CuteQStackedLayoutCall10)(const void *, int, int *);
typedef void (*CuteQStackedLayoutCall11)(const void *, int *);
typedef const QRect * (*CuteQStackedLayoutCall12)(const void *, int *);
typedef const QSize * (*CuteQStackedLayoutCall13)(const void *, int *);
typedef int (*CuteQStackedLayoutCall14)(const void *, const QWidget *, int *);
typedef int (*CuteQStackedLayoutCall15)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQStackedLayoutCall16)(const void *, int *);
typedef void * (*CuteQStackedLayoutCall17)(const void *, int *);
typedef void (*CuteQStackedLayoutCall18)(const void *, QChildEvent *, int *);
typedef bool (*CuteQStackedLayoutCall19)(const void *, QEvent *, int *);
typedef bool (*CuteQStackedLayoutCall20)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQStackedLayoutCall21)(const void *, QTimerEvent *, int *);
typedef void (*CuteQStackedLayoutCall22)(const void *, QEvent *, int *);
typedef void (*CuteQStackedLayoutCall23)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQStackedLayoutCall24)(const void *, const QMetaMethod *, int *);
typedef int (*CuteQStackedLayoutCall25)(const void *, int, int *);
typedef void * (*CuteQStackedLayoutCall26)(const void *, int *);
typedef void * (*CuteQStackedLayoutCall27)(const void *, int *);
class CuteQStackedLayout : public QStackedLayout {
public:
  using QStackedLayout::QStackedLayout;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
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
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[27] = call;
      return true;
    }
    return false;
  }

  //  int QStackedLayout::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStackedLayoutCall0 call = reinterpret_cast<CuteQStackedLayoutCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QStackedLayout::count();
  }

  //  void QStackedLayout::addItem(QLayoutItem *item)
  void addItem(QLayoutItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStackedLayoutCall1 call = reinterpret_cast<CuteQStackedLayoutCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QStackedLayout::addItem(item);
  }

  //  QSize QStackedLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQStackedLayoutCall2 call = reinterpret_cast<CuteQStackedLayoutCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStackedLayout::sizeHint();
  }

  //  QSize QStackedLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStackedLayoutCall3 call = reinterpret_cast<CuteQStackedLayoutCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStackedLayout::minimumSize();
  }

  //  QLayoutItem *QStackedLayout::itemAt(int a0) const
  QLayoutItem *itemAt(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStackedLayoutCall4 call = reinterpret_cast<CuteQStackedLayoutCall4>(taken[4]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QStackedLayout::itemAt(a0);
  }

  //  QLayoutItem *QStackedLayout::takeAt(int a0)
  QLayoutItem *takeAt(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStackedLayoutCall5 call = reinterpret_cast<CuteQStackedLayoutCall5>(taken[5]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QStackedLayout::takeAt(a0);
  }

  //  void QStackedLayout::setGeometry(const QRect &rect)
  void setGeometry(const QRect &rect) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStackedLayoutCall6 call = reinterpret_cast<CuteQStackedLayoutCall6>(taken[6]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QStackedLayout::setGeometry(rect);
  }

  //  bool QStackedLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStackedLayoutCall7 call = reinterpret_cast<CuteQStackedLayoutCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QStackedLayout::hasHeightForWidth();
  }

  //  int QStackedLayout::heightForWidth(int width) const
  int heightForWidth(int width) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStackedLayoutCall8 call = reinterpret_cast<CuteQStackedLayoutCall8>(taken[8]);
      int given = call(this, width, &handled);
      if (handled) return given;
    }
    return QStackedLayout::heightForWidth(width);
  }

  //  int QLayout::spacing() const
  int spacing() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStackedLayoutCall9 call = reinterpret_cast<CuteQStackedLayoutCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::spacing();
  }

  //  void QLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStackedLayoutCall10 call = reinterpret_cast<CuteQStackedLayoutCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLayout::setSpacing(a0);
  }

  //  void QLayout::invalidate()
  void invalidate() override {
    if (taken[11]) {
      int handled = 0;
      CuteQStackedLayoutCall11 call = reinterpret_cast<CuteQStackedLayoutCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QLayout::invalidate();
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQStackedLayoutCall12 call = reinterpret_cast<CuteQStackedLayoutCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  QSize QLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQStackedLayoutCall13 call = reinterpret_cast<CuteQStackedLayoutCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::maximumSize();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQStackedLayoutCall14 call = reinterpret_cast<CuteQStackedLayoutCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQStackedLayoutCall15 call = reinterpret_cast<CuteQStackedLayoutCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQStackedLayoutCall16 call = reinterpret_cast<CuteQStackedLayoutCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[17]) {
      int handled = 0;
      CuteQStackedLayoutCall17 call = reinterpret_cast<CuteQStackedLayoutCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQStackedLayoutCall18 call = reinterpret_cast<CuteQStackedLayoutCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQStackedLayoutCall19 call = reinterpret_cast<CuteQStackedLayoutCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQStackedLayoutCall20 call = reinterpret_cast<CuteQStackedLayoutCall20>(taken[20]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQStackedLayoutCall21 call = reinterpret_cast<CuteQStackedLayoutCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQStackedLayoutCall22 call = reinterpret_cast<CuteQStackedLayoutCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQStackedLayoutCall23 call = reinterpret_cast<CuteQStackedLayoutCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStackedLayoutCall24 call = reinterpret_cast<CuteQStackedLayoutCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQStackedLayoutCall25 call = reinterpret_cast<CuteQStackedLayoutCall25>(taken[25]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQStackedLayoutCall26 call = reinterpret_cast<CuteQStackedLayoutCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[27]) {
      int handled = 0;
      CuteQStackedLayoutCall27 call = reinterpret_cast<CuteQStackedLayoutCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QStackedLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QStackedLayout10metaObjectEv(
    const QStackedLayout *self) {
  return self->metaObject();
}

//  QString QStackedLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStackedLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedLayout::tr(s, c, n));
}

//  QStackedLayout::QStackedLayout()
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1Ev() {
  return new CuteQStackedLayout();
}

//  QStackedLayout::QStackedLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1EP7QWidget(QWidget *parent) {
  return new CuteQStackedLayout(parent);
}

//  QStackedLayout::QStackedLayout(QLayout *parentLayout)
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1EP7QLayout(
    QLayout *parentLayout) {
  return new CuteQStackedLayout(parentLayout);
}

//  QStackedLayout::~QStackedLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayoutD1Ev(QStackedLayout *self) {
  delete self;
}

//  int QStackedLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedLayout9addWidgetEP7QWidget(
    QStackedLayout *self,
    QWidget *w) {
  return self->addWidget(w);
}

//  int QStackedLayout::insertWidget(int index, QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedLayout12insertWidgetEiP7QWidget(
    QStackedLayout *self,
    int index,
    QWidget *w) {
  return self->insertWidget(index, w);
}

//  QWidget *QStackedLayout::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedLayout13currentWidgetEv(
    const QStackedLayout *self) {
  return self->currentWidget();
}

//  int QStackedLayout::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout12currentIndexEv(const QStackedLayout *self) {
  return self->currentIndex();
}

//  QWidget *QStackedLayout::widget(int a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedLayout6widgetEi(
    const QStackedLayout *self,
    int a0) {
  return self->widget(a0);
}

//  int QStackedLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout5countEv(const QStackedLayout *self) {
  return self->count();
}

//  StackingMode QStackedLayout::stackingMode() const
extern "C" Q_DECL_EXPORT
QStackedLayout::StackingMode ritual_ZNK14QStackedLayout12stackingModeEv(
    const QStackedLayout *self) {
  return self->stackingMode();
}

//  void QStackedLayout::setStackingMode(StackingMode stackingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout15setStackingModeENS_12StackingModeE(
    QStackedLayout *self,
    QStackedLayout::StackingMode stackingMode) {
  self->setStackingMode(stackingMode);
}

//  void QStackedLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout7addItemEP11QLayoutItem(
    QStackedLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  QSize QStackedLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QStackedLayout8sizeHintEv(const QStackedLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QStackedLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QStackedLayout11minimumSizeEv(
    const QStackedLayout *self) {
  return new QSize(self->minimumSize());
}

//  QLayoutItem *QStackedLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK14QStackedLayout6itemAtEi(
    const QStackedLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  QLayoutItem *QStackedLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN14QStackedLayout6takeAtEi(
    QStackedLayout *self,
    int a0) {
  return self->takeAt(a0);
}

//  void QStackedLayout::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout11setGeometryERK5QRect(
    QStackedLayout *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  bool QStackedLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QStackedLayout17hasHeightForWidthEv(
    const QStackedLayout *self) {
  return self->hasHeightForWidth();
}

//  int QStackedLayout::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout14heightForWidthEi(
    const QStackedLayout *self,
    int width) {
  return self->heightForWidth(width);
}

//  void QStackedLayout::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout15setCurrentIndexEi(
    QStackedLayout *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QStackedLayout::setCurrentWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout16setCurrentWidgetEP7QWidget(
    QStackedLayout *self,
    QWidget *w) {
  self->setCurrentWidget(w);
}

//  a Python function taken by a CuteQStackedLayout, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStackedLayout(
    QStackedLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStackedLayout *>(self)->take(key, call);
}

//  int QStackedLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QStackedLayout5countEv(const QStackedLayout *self) {
  return self->QStackedLayout::count();
}

//  void QStackedLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStackedLayout7addItemEP11QLayoutItem(
    QStackedLayout *self,
    QLayoutItem *item) {
  self->QStackedLayout::addItem(item);
}

//  QSize QStackedLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QStackedLayout8sizeHintEv(
    const QStackedLayout *self) {
  return new QSize(self->QStackedLayout::sizeHint());
}

//  QSize QStackedLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QStackedLayout11minimumSizeEv(
    const QStackedLayout *self) {
  return new QSize(self->QStackedLayout::minimumSize());
}

//  QLayoutItem *QStackedLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK14QStackedLayout6itemAtEi(
    const QStackedLayout *self,
    int a0) {
  return self->QStackedLayout::itemAt(a0);
}

//  QLayoutItem *QStackedLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN14QStackedLayout6takeAtEi(
    QStackedLayout *self,
    int a0) {
  return self->QStackedLayout::takeAt(a0);
}

//  void QStackedLayout::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStackedLayout11setGeometryERK5QRect(
    QStackedLayout *self,
    const QRect *rect) {
  self->QStackedLayout::setGeometry(*rect);
}

//  bool QStackedLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QStackedLayout17hasHeightForWidthEv(
    const QStackedLayout *self) {
  return self->QStackedLayout::hasHeightForWidth();
}

//  int QStackedLayout::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QStackedLayout14heightForWidthEi(
    const QStackedLayout *self,
    int width) {
  return self->QStackedLayout::heightForWidth(width);
}
