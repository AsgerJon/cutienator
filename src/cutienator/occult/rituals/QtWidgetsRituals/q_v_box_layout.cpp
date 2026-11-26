//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVBoxLayout that Python can take functions over in. Every QVBoxLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVBoxLayoutCall0)(const void *, QLayoutItem *, int *);
typedef int (*CuteQVBoxLayoutCall1)(const void *, int *);
typedef void (*CuteQVBoxLayoutCall2)(const void *, int, int *);
typedef const QSize * (*CuteQVBoxLayoutCall3)(const void *, int *);
typedef const QSize * (*CuteQVBoxLayoutCall4)(const void *, int *);
typedef const QSize * (*CuteQVBoxLayoutCall5)(const void *, int *);
typedef bool (*CuteQVBoxLayoutCall6)(const void *, int *);
typedef int (*CuteQVBoxLayoutCall7)(const void *, int, int *);
typedef int (*CuteQVBoxLayoutCall8)(const void *, int, int *);
typedef int (*CuteQVBoxLayoutCall9)(const void *, int *);
typedef void (*CuteQVBoxLayoutCall10)(const void *, int *);
typedef void * (*CuteQVBoxLayoutCall11)(const void *, int, int *);
typedef void * (*CuteQVBoxLayoutCall12)(const void *, int, int *);
typedef int (*CuteQVBoxLayoutCall13)(const void *, int *);
typedef void (*CuteQVBoxLayoutCall14)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQVBoxLayoutCall15)(const void *, int *);
typedef int (*CuteQVBoxLayoutCall16)(const void *, const QWidget *, int *);
typedef int (*CuteQVBoxLayoutCall17)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQVBoxLayoutCall18)(const void *, int *);
typedef int (*CuteQVBoxLayoutCall19)(const void *, int *);
typedef void * (*CuteQVBoxLayoutCall20)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQVBoxLayoutCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxLayoutCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBoxLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBoxLayoutCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxLayoutCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxLayoutCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxLayoutCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxLayoutCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQVBoxLayoutCall29)(const void *, int *);
typedef void * (*CuteQVBoxLayoutCall30)(const void *, int *);
class CuteQVBoxLayout : public QVBoxLayout {
public:
  using QVBoxLayout::QVBoxLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  void QBoxLayout::addItem(QLayoutItem *a0)
  void addItem(QLayoutItem *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQVBoxLayoutCall0 call = reinterpret_cast<CuteQVBoxLayoutCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QBoxLayout::addItem(a0);
  }

  //  int QBoxLayout::spacing() const
  int spacing() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVBoxLayoutCall1 call = reinterpret_cast<CuteQVBoxLayoutCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::spacing();
  }

  //  void QBoxLayout::setSpacing(int spacing)
  void setSpacing(int spacing) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVBoxLayoutCall2 call = reinterpret_cast<CuteQVBoxLayoutCall2>(taken[2]);
      call(this, spacing, &handled);
      if (handled) return;
    }
    QBoxLayout::setSpacing(spacing);
  }

  //  QSize QBoxLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVBoxLayoutCall3 call = reinterpret_cast<CuteQVBoxLayoutCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::sizeHint();
  }

  //  QSize QBoxLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVBoxLayoutCall4 call = reinterpret_cast<CuteQVBoxLayoutCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::minimumSize();
  }

  //  QSize QBoxLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVBoxLayoutCall5 call = reinterpret_cast<CuteQVBoxLayoutCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::maximumSize();
  }

  //  bool QBoxLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVBoxLayoutCall6 call = reinterpret_cast<CuteQVBoxLayoutCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::hasHeightForWidth();
  }

  //  int QBoxLayout::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQVBoxLayoutCall7 call = reinterpret_cast<CuteQVBoxLayoutCall7>(taken[7]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::heightForWidth(a0);
  }

  //  int QBoxLayout::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQVBoxLayoutCall8 call = reinterpret_cast<CuteQVBoxLayoutCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::minimumHeightForWidth(a0);
  }

  //  Qt::Orientations QBoxLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQVBoxLayoutCall9 call = reinterpret_cast<CuteQVBoxLayoutCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QBoxLayout::expandingDirections();
  }

  //  void QBoxLayout::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQVBoxLayoutCall10 call = reinterpret_cast<CuteQVBoxLayoutCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxLayout::invalidate();
  }

  //  QLayoutItem *QBoxLayout::itemAt(int a0) const
  QLayoutItem *itemAt(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQVBoxLayoutCall11 call = reinterpret_cast<CuteQVBoxLayoutCall11>(taken[11]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::itemAt(a0);
  }

  //  QLayoutItem *QBoxLayout::takeAt(int a0)
  QLayoutItem *takeAt(int a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQVBoxLayoutCall12 call = reinterpret_cast<CuteQVBoxLayoutCall12>(taken[12]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::takeAt(a0);
  }

  //  int QBoxLayout::count() const
  int count() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQVBoxLayoutCall13 call = reinterpret_cast<CuteQVBoxLayoutCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::count();
  }

  //  void QBoxLayout::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQVBoxLayoutCall14 call = reinterpret_cast<CuteQVBoxLayoutCall14>(taken[14]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QBoxLayout::setGeometry(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQVBoxLayoutCall15 call = reinterpret_cast<CuteQVBoxLayoutCall15>(taken[15]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQVBoxLayoutCall16 call = reinterpret_cast<CuteQVBoxLayoutCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQVBoxLayoutCall17 call = reinterpret_cast<CuteQVBoxLayoutCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQVBoxLayoutCall18 call = reinterpret_cast<CuteQVBoxLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQVBoxLayoutCall19 call = reinterpret_cast<CuteQVBoxLayoutCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQVBoxLayoutCall20 call = reinterpret_cast<CuteQVBoxLayoutCall20>(taken[20]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[21]) {
      int handled = 0;
      CuteQVBoxLayoutCall21 call = reinterpret_cast<CuteQVBoxLayoutCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQVBoxLayoutCall22 call = reinterpret_cast<CuteQVBoxLayoutCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQVBoxLayoutCall23 call = reinterpret_cast<CuteQVBoxLayoutCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQVBoxLayoutCall24 call = reinterpret_cast<CuteQVBoxLayoutCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQVBoxLayoutCall25 call = reinterpret_cast<CuteQVBoxLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQVBoxLayoutCall26 call = reinterpret_cast<CuteQVBoxLayoutCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQVBoxLayoutCall27 call = reinterpret_cast<CuteQVBoxLayoutCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQVBoxLayoutCall28 call = reinterpret_cast<CuteQVBoxLayoutCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQVBoxLayoutCall29 call = reinterpret_cast<CuteQVBoxLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQVBoxLayoutCall30 call = reinterpret_cast<CuteQVBoxLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QVBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QVBoxLayout10metaObjectEv(
    const QVBoxLayout *self) {
  return self->metaObject();
}

//  void *QVBoxLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QVBoxLayout11qt_metacastEPKc(
    QVBoxLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVBoxLayout::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QVBoxLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QVBoxLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QVBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVBoxLayout::tr(s, c, n));
}

//  QVBoxLayout::QVBoxLayout()
extern "C" Q_DECL_EXPORT
QVBoxLayout *ritual_ZN11QVBoxLayoutC1Ev() {
  return new CuteQVBoxLayout();
}

//  QVBoxLayout::QVBoxLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QVBoxLayout *ritual_ZN11QVBoxLayoutC1EP7QWidget(QWidget *parent) {
  return new CuteQVBoxLayout(parent);
}

//  QVBoxLayout::~QVBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVBoxLayoutD1Ev(QVBoxLayout *self) {
  delete self;
}

//  a Python function taken by a CuteQVBoxLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVBoxLayout(
    QVBoxLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVBoxLayout *>(self)->take(key, call);
}
