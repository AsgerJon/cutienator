//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLayout : QLayout {
  using QLayout::childEvent;
};

//  A QLayout that Python can take functions over in. Every QLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQLayoutCall0)(const void *, int *);
typedef void (*CuteQLayoutCall1)(const void *, int, int *);
typedef void (*CuteQLayoutCall2)(const void *, int *);
typedef const QRect * (*CuteQLayoutCall3)(const void *, int *);
typedef void (*CuteQLayoutCall4)(const void *, QLayoutItem *, int *);
typedef int (*CuteQLayoutCall5)(const void *, int *);
typedef const QSize * (*CuteQLayoutCall6)(const void *, int *);
typedef const QSize * (*CuteQLayoutCall7)(const void *, int *);
typedef void (*CuteQLayoutCall8)(const void *, const QRect *, int *);
typedef void * (*CuteQLayoutCall9)(const void *, int, int *);
typedef void * (*CuteQLayoutCall10)(const void *, int, int *);
typedef int (*CuteQLayoutCall11)(const void *, const QWidget *, int *);
typedef int (*CuteQLayoutCall12)(const void *, const QLayoutItem *, int *);
typedef int (*CuteQLayoutCall13)(const void *, int *);
typedef bool (*CuteQLayoutCall14)(const void *, int *);
typedef int (*CuteQLayoutCall15)(const void *, int *);
typedef void * (*CuteQLayoutCall16)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQLayoutCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLayoutCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLayoutCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLayoutCall20)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLayoutCall21)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLayoutCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLayoutCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLayoutCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef const QSize * (*CuteQLayoutCall25)(const void *, int *);
typedef bool (*CuteQLayoutCall26)(const void *, int *);
typedef int (*CuteQLayoutCall27)(const void *, int, int *);
typedef int (*CuteQLayoutCall28)(const void *, int, int *);
typedef void * (*CuteQLayoutCall29)(const void *, int *);
typedef void * (*CuteQLayoutCall30)(const void *, int *);
class CuteQLayout : public QLayout {
public:
  using QLayout::QLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[30] = call;
      return true;
    }
    return false;
  }

  //  int QLayout::spacing() const
  int spacing() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLayoutCall0 call = reinterpret_cast<CuteQLayoutCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::spacing();
  }

  //  void QLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLayoutCall1 call = reinterpret_cast<CuteQLayoutCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLayout::setSpacing(a0);
  }

  //  void QLayout::invalidate()
  void invalidate() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLayoutCall2 call = reinterpret_cast<CuteQLayoutCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QLayout::invalidate();
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLayoutCall3 call = reinterpret_cast<CuteQLayoutCall3>(taken[3]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  void QLayout::addItem(QLayoutItem *a0)
  void addItem(QLayoutItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLayoutCall4 call = reinterpret_cast<CuteQLayoutCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  Qt::Orientations QLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLayoutCall5 call = reinterpret_cast<CuteQLayoutCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QLayout::expandingDirections();
  }

  //  QSize QLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLayoutCall6 call = reinterpret_cast<CuteQLayoutCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::minimumSize();
  }

  //  QSize QLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLayoutCall7 call = reinterpret_cast<CuteQLayoutCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::maximumSize();
  }

  //  void QLayout::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLayoutCall8 call = reinterpret_cast<CuteQLayoutCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLayout::setGeometry(a0);
  }

  //  QLayoutItem *QLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLayoutCall9 call = reinterpret_cast<CuteQLayoutCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return {};
  }

  //  QLayoutItem *QLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLayoutCall10 call = reinterpret_cast<CuteQLayoutCall10>(taken[10]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return {};
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLayoutCall11 call = reinterpret_cast<CuteQLayoutCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLayoutCall12 call = reinterpret_cast<CuteQLayoutCall12>(taken[12]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::count() const
  int count() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQLayoutCall13 call = reinterpret_cast<CuteQLayoutCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQLayoutCall14 call = reinterpret_cast<CuteQLayoutCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQLayoutCall15 call = reinterpret_cast<CuteQLayoutCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayout::controlTypes();
  }

  //  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
  //      Qt::FindChildOptions options)
  QLayoutItem *replaceWidget(
      QWidget *from,
      QWidget *to,
      Qt::FindChildOptions options) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLayoutCall16 call = reinterpret_cast<CuteQLayoutCall16>(taken[16]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[17]) {
      int handled = 0;
      CuteQLayoutCall17 call = reinterpret_cast<CuteQLayoutCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLayoutCall18 call = reinterpret_cast<CuteQLayoutCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLayoutCall19 call = reinterpret_cast<CuteQLayoutCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLayoutCall20 call = reinterpret_cast<CuteQLayoutCall20>(taken[20]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLayoutCall21 call = reinterpret_cast<CuteQLayoutCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLayoutCall22 call = reinterpret_cast<CuteQLayoutCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLayoutCall23 call = reinterpret_cast<CuteQLayoutCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLayoutCall24 call = reinterpret_cast<CuteQLayoutCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSize QLayoutItem::sizeHint() const
  QSize sizeHint() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQLayoutCall25 call = reinterpret_cast<CuteQLayoutCall25>(taken[25]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QLayoutItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQLayoutCall26 call = reinterpret_cast<CuteQLayoutCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQLayoutCall27 call = reinterpret_cast<CuteQLayoutCall27>(taken[27]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQLayoutCall28 call = reinterpret_cast<CuteQLayoutCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQLayoutCall29 call = reinterpret_cast<CuteQLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQLayoutCall30 call = reinterpret_cast<CuteQLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QLayout10metaObjectEv(const QLayout *self) {
  return self->metaObject();
}

//  QString QLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLayout2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLayout::tr(s, c, n));
}

//  QLayoutPrivate *QLayout::d_func()
extern "C" Q_DECL_EXPORT
QLayoutPrivate *ritual_ZN7QLayout6d_funcEv(QLayout *self) {
  return self->d_func();
}

//  const QLayoutPrivate *QLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QLayoutPrivate *ritual_ZNK7QLayout6d_funcEv(const QLayout *self) {
  return self->d_func();
}

//  QLayout::~QLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayoutD1Ev(QLayout *self) {
  delete self;
}

//  int QLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7spacingEv(const QLayout *self) {
  return self->spacing();
}

//  void QLayout::setSpacing(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setSpacingEi(QLayout *self, int a0) {
  self->setSpacing(a0);
}

//  void QLayout::setContentsMargins(int left, int top, int right, int
//      bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setContentsMarginsEiiii(
    QLayout *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QLayout::setContentsMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setContentsMarginsERK8QMargins(
    QLayout *self,
    const QMargins *margins) {
  self->setContentsMargins(*margins);
}

//  void QLayout::unsetContentsMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout20unsetContentsMarginsEv(QLayout *self) {
  self->unsetContentsMargins();
}

//  void QLayout::getContentsMargins(int *left, int *top, int *right, int
//      *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QLayout18getContentsMarginsEPiS0_S0_S0_(
    const QLayout *self,
    int *left,
    int *top,
    int *right,
    int *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  QMargins QLayout::contentsMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QLayout15contentsMarginsEv(const QLayout *self) {
  return new QMargins(self->contentsMargins());
}

//  QRect QLayout::contentsRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QLayout12contentsRectEv(const QLayout *self) {
  return new QRect(self->contentsRect());
}

//  bool QLayout::setAlignment(QWidget *w, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout12setAlignmentEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    QLayout *self,
    QWidget *w,
    int alignment) {
  return self->setAlignment(
      w,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  bool QLayout::setAlignment(QLayout *l, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout12setAlignmentEPS_6QFlagsIN2Qt13AlignmentFlagEE(
    QLayout *self,
    QLayout *l,
    int alignment) {
  return self->setAlignment(
      l,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QLayout::setSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout17setSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setSizeConstraint(constraint);
}

//  SizeConstraint QLayout::sizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout14sizeConstraintEv(
    const QLayout *self) {
  return self->sizeConstraint();
}

//  void QLayout::setSizeConstraints(SizeConstraint horizontal,
//      SizeConstraint vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setSizeConstraintsENS_14SizeConstraintES0_(
    QLayout *self,
    QLayout::SizeConstraint horizontal,
    QLayout::SizeConstraint vertical) {
  self->setSizeConstraints(horizontal, vertical);
}

//  void QLayout::setHorizontalSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout27setHorizontalSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setHorizontalSizeConstraint(constraint);
}

//  SizeConstraint QLayout::horizontalSizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout24horizontalSizeConstraintEv(
    const QLayout *self) {
  return self->horizontalSizeConstraint();
}

//  void QLayout::setVerticalSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout25setVerticalSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setVerticalSizeConstraint(constraint);
}

//  SizeConstraint QLayout::verticalSizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout22verticalSizeConstraintEv(
    const QLayout *self) {
  return self->verticalSizeConstraint();
}

//  void QLayout::setMenuBar(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setMenuBarEP7QWidget(QLayout *self, QWidget *w) {
  self->setMenuBar(w);
}

//  QWidget *QLayout::menuBar() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QLayout7menuBarEv(const QLayout *self) {
  return self->menuBar();
}

//  QWidget *QLayout::parentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QLayout12parentWidgetEv(const QLayout *self) {
  return self->parentWidget();
}

//  void QLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10invalidateEv(QLayout *self) {
  self->invalidate();
}

//  QRect QLayout::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QLayout8geometryEv(const QLayout *self) {
  return new QRect(self->geometry());
}

//  bool QLayout::activate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout8activateEv(QLayout *self) {
  return self->activate();
}

//  void QLayout::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout6updateEv(QLayout *self) {
  self->update();
}

//  void QLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout9addWidgetEP7QWidget(QLayout *self, QWidget *w) {
  self->addWidget(w);
}

//  void QLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout7addItemEP11QLayoutItem(
    QLayout *self,
    QLayoutItem *a0) {
  self->addItem(a0);
}

//  void QLayout::removeWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout12removeWidgetEP7QWidget(QLayout *self, QWidget *w) {
  self->removeWidget(w);
}

//  void QLayout::removeItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10removeItemEP11QLayoutItem(
    QLayout *self,
    QLayoutItem *a0) {
  self->removeItem(a0);
}

//  Qt::Orientations QLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout19expandingDirectionsEv(const QLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  QSize QLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout11minimumSizeEv(const QLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout11maximumSizeEv(const QLayout *self) {
  return new QSize(self->maximumSize());
}

//  void QLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout11setGeometryERK5QRect(
    QLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QLayoutItem *QLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK7QLayout6itemAtEi(const QLayout *self, int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN7QLayout6takeAtEi(QLayout *self, int index) {
  return self->takeAt(index);
}

//  int QLayout::indexOf(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7indexOfEPK7QWidget(
    const QLayout *self,
    const QWidget *a0) {
  return self->indexOf(a0);
}

//  int QLayout::indexOf(const QLayoutItem *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7indexOfEPK11QLayoutItem(
    const QLayout *self,
    const QLayoutItem *a0) {
  return self->indexOf(a0);
}

//  int QLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout5countEv(const QLayout *self) {
  return self->count();
}

//  bool QLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLayout7isEmptyEv(const QLayout *self) {
  return self->isEmpty();
}

//  QSizePolicy::ControlTypes QLayout::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout12controlTypesEv(const QLayout *self) {
  return static_cast<int>(self->controlTypes().toInt());
}

//  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
//      Qt::FindChildOptions options)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE(
    QLayout *self,
    QWidget *from,
    QWidget *to,
    int options) {
  return self->replaceWidget(
      from,
      to,
      QFlags<Qt::FindChildOption>::fromInt(options));
}

//  int QLayout::totalMinimumHeightForWidth(int w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout26totalMinimumHeightForWidthEi(
    const QLayout *self,
    int w) {
  return self->totalMinimumHeightForWidth(w);
}

//  int QLayout::totalHeightForWidth(int w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout19totalHeightForWidthEi(const QLayout *self, int w) {
  return self->totalHeightForWidth(w);
}

//  QSize QLayout::totalMinimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout16totalMinimumSizeEv(const QLayout *self) {
  return new QSize(self->totalMinimumSize());
}

//  QSize QLayout::totalMaximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout16totalMaximumSizeEv(const QLayout *self) {
  return new QSize(self->totalMaximumSize());
}

//  QSize QLayout::totalSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout13totalSizeHintEv(const QLayout *self) {
  return new QSize(self->totalSizeHint());
}

//  QLayout *QLayout::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN7QLayout6layoutEv(QLayout *self) {
  return self->layout();
}

//  void QLayout::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setEnabledEb(QLayout *self, bool a0) {
  self->setEnabled(a0);
}

//  bool QLayout::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLayout9isEnabledEv(const QLayout *self) {
  return self->isEnabled();
}

//  QSize QLayout::closestAcceptableSize(const QWidget *w, const QSize &s)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN7QLayout21closestAcceptableSizeEPK7QWidgetRK5QSize(
    const QWidget *w,
    const QSize *s) {
  return new QSize(QLayout::closestAcceptableSize(w, *s));
}

//  void QLayout::widgetEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout11widgetEventEP6QEvent(QLayout *self, QEvent *a0) {
  self->widgetEvent(a0);
}

//  void QLayout::childEvent(QChildEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10childEventEP11QChildEvent(
    QLayout *self,
    QChildEvent *e) {
  self->childEvent(e);
}

//  void QLayout::addChildLayout(QLayout *l)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout14addChildLayoutEPS_(QLayout *self, QLayout *l) {
  self->addChildLayout(l);
}

//  void QLayout::addChildWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout14addChildWidgetEP7QWidget(QLayout *self, QWidget *w) {
  self->addChildWidget(w);
}

//  bool QLayout::adoptLayout(QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout11adoptLayoutEPS_(QLayout *self, QLayout *layout) {
  return self->adoptLayout(layout);
}

//  QRect QLayout::alignmentRect(const QRect &a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QLayout13alignmentRectERK5QRect(
    const QLayout *self,
    const QRect *a0) {
  return new QRect(self->alignmentRect(*a0));
}

//  void QLayout::activateRecursiveHelper(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout23activateRecursiveHelperEP11QLayoutItem(
    QLayoutItem *item) {
  QLayout::activateRecursiveHelper(item);
}

//  QLayout as the QLayoutItem it is built on
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_cast_QLayout_QLayoutItem(QLayout *self) {
  return static_cast<QLayoutItem *>(self);
}

//  a Python function taken by a CuteQLayout, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLayout(QLayout *self, const char *key, void *call) {
  return static_cast<CuteQLayout *>(self)->take(key, call);
}

//  int QLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QLayout7spacingEv(const QLayout *self) {
  return self->QLayout::spacing();
}

//  void QLayout::setSpacing(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLayout10setSpacingEi(QLayout *self, int a0) {
  self->QLayout::setSpacing(a0);
}

//  void QLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLayout10invalidateEv(QLayout *self) {
  self->QLayout::invalidate();
}

//  QRect QLayout::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK7QLayout8geometryEv(const QLayout *self) {
  return new QRect(self->QLayout::geometry());
}

//  Qt::Orientations QLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QLayout19expandingDirectionsEv(const QLayout *self) {
  return static_cast<int>(self->QLayout::expandingDirections().toInt());
}

//  QSize QLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QLayout11minimumSizeEv(const QLayout *self) {
  return new QSize(self->QLayout::minimumSize());
}

//  QSize QLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QLayout11maximumSizeEv(const QLayout *self) {
  return new QSize(self->QLayout::maximumSize());
}

//  void QLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLayout11setGeometryERK5QRect(
    QLayout *self,
    const QRect *a0) {
  self->QLayout::setGeometry(*a0);
}

//  int QLayout::indexOf(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QLayout7indexOfEPK7QWidget(
    const QLayout *self,
    const QWidget *a0) {
  return self->QLayout::indexOf(a0);
}

//  int QLayout::indexOf(const QLayoutItem *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QLayout7indexOfEPK11QLayoutItem(
    const QLayout *self,
    const QLayoutItem *a0) {
  return self->QLayout::indexOf(a0);
}

//  bool QLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK7QLayout7isEmptyEv(const QLayout *self) {
  return self->QLayout::isEmpty();
}

//  QSizePolicy::ControlTypes QLayout::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QLayout12controlTypesEv(const QLayout *self) {
  return static_cast<int>(self->QLayout::controlTypes().toInt());
}

//  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
//      Qt::FindChildOptions options)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE(
    QLayout *self,
    QWidget *from,
    QWidget *to,
    int options) {
  return self->QLayout::replaceWidget(
      from,
      to,
      QFlags<Qt::FindChildOption>::fromInt(options));
}

//  QLayout *QLayout::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN7QLayout6layoutEv(QLayout *self) {
  return self->QLayout::layout();
}

//  void QLayout::childEvent(QChildEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLayout10childEventEP11QChildEvent(
    QLayout *self,
    QChildEvent *e) {
  static_cast<OwnQLayout *>(self)->OwnQLayout::childEvent(e);
}
