//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHBoxLayout that Python can take functions over in. Every QHBoxLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHBoxLayoutCall0)(const void *, QLayoutItem *, int *);
typedef int (*CuteQHBoxLayoutCall1)(const void *, int *);
typedef void (*CuteQHBoxLayoutCall2)(const void *, int, int *);
typedef const QSize * (*CuteQHBoxLayoutCall3)(const void *, int *);
typedef const QSize * (*CuteQHBoxLayoutCall4)(const void *, int *);
typedef const QSize * (*CuteQHBoxLayoutCall5)(const void *, int *);
typedef bool (*CuteQHBoxLayoutCall6)(const void *, int *);
typedef int (*CuteQHBoxLayoutCall7)(const void *, int, int *);
typedef int (*CuteQHBoxLayoutCall8)(const void *, int, int *);
typedef int (*CuteQHBoxLayoutCall9)(const void *, int *);
typedef void (*CuteQHBoxLayoutCall10)(const void *, int *);
typedef void * (*CuteQHBoxLayoutCall11)(const void *, int, int *);
typedef void * (*CuteQHBoxLayoutCall12)(const void *, int, int *);
typedef int (*CuteQHBoxLayoutCall13)(const void *, int *);
typedef void (*CuteQHBoxLayoutCall14)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQHBoxLayoutCall15)(const void *, int *);
typedef int (*CuteQHBoxLayoutCall16)(const void *, const QWidget *, int *);
typedef int (*CuteQHBoxLayoutCall17)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQHBoxLayoutCall18)(const void *, int *);
typedef int (*CuteQHBoxLayoutCall19)(const void *, int *);
typedef void * (*CuteQHBoxLayoutCall20)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQHBoxLayoutCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxLayoutCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBoxLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBoxLayoutCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxLayoutCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxLayoutCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxLayoutCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxLayoutCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQHBoxLayoutCall29)(const void *, int *);
typedef void * (*CuteQHBoxLayoutCall30)(const void *, int *);
class CuteQHBoxLayout : public QHBoxLayout {
public:
  using QHBoxLayout::QHBoxLayout;
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
      CuteQHBoxLayoutCall0 call = reinterpret_cast<CuteQHBoxLayoutCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QBoxLayout::addItem(a0);
  }

  //  int QBoxLayout::spacing() const
  int spacing() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHBoxLayoutCall1 call = reinterpret_cast<CuteQHBoxLayoutCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::spacing();
  }

  //  void QBoxLayout::setSpacing(int spacing)
  void setSpacing(int spacing) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHBoxLayoutCall2 call = reinterpret_cast<CuteQHBoxLayoutCall2>(taken[2]);
      call(this, spacing, &handled);
      if (handled) return;
    }
    QBoxLayout::setSpacing(spacing);
  }

  //  QSize QBoxLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHBoxLayoutCall3 call = reinterpret_cast<CuteQHBoxLayoutCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::sizeHint();
  }

  //  QSize QBoxLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHBoxLayoutCall4 call = reinterpret_cast<CuteQHBoxLayoutCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::minimumSize();
  }

  //  QSize QBoxLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHBoxLayoutCall5 call = reinterpret_cast<CuteQHBoxLayoutCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::maximumSize();
  }

  //  bool QBoxLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHBoxLayoutCall6 call = reinterpret_cast<CuteQHBoxLayoutCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::hasHeightForWidth();
  }

  //  int QBoxLayout::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHBoxLayoutCall7 call = reinterpret_cast<CuteQHBoxLayoutCall7>(taken[7]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::heightForWidth(a0);
  }

  //  int QBoxLayout::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQHBoxLayoutCall8 call = reinterpret_cast<CuteQHBoxLayoutCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::minimumHeightForWidth(a0);
  }

  //  Qt::Orientations QBoxLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQHBoxLayoutCall9 call = reinterpret_cast<CuteQHBoxLayoutCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QBoxLayout::expandingDirections();
  }

  //  void QBoxLayout::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQHBoxLayoutCall10 call = reinterpret_cast<CuteQHBoxLayoutCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxLayout::invalidate();
  }

  //  QLayoutItem *QBoxLayout::itemAt(int a0) const
  QLayoutItem *itemAt(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQHBoxLayoutCall11 call = reinterpret_cast<CuteQHBoxLayoutCall11>(taken[11]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::itemAt(a0);
  }

  //  QLayoutItem *QBoxLayout::takeAt(int a0)
  QLayoutItem *takeAt(int a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHBoxLayoutCall12 call = reinterpret_cast<CuteQHBoxLayoutCall12>(taken[12]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::takeAt(a0);
  }

  //  int QBoxLayout::count() const
  int count() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHBoxLayoutCall13 call = reinterpret_cast<CuteQHBoxLayoutCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::count();
  }

  //  void QBoxLayout::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHBoxLayoutCall14 call = reinterpret_cast<CuteQHBoxLayoutCall14>(taken[14]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QBoxLayout::setGeometry(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQHBoxLayoutCall15 call = reinterpret_cast<CuteQHBoxLayoutCall15>(taken[15]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQHBoxLayoutCall16 call = reinterpret_cast<CuteQHBoxLayoutCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQHBoxLayoutCall17 call = reinterpret_cast<CuteQHBoxLayoutCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQHBoxLayoutCall18 call = reinterpret_cast<CuteQHBoxLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQHBoxLayoutCall19 call = reinterpret_cast<CuteQHBoxLayoutCall19>(taken[19]);
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
      CuteQHBoxLayoutCall20 call = reinterpret_cast<CuteQHBoxLayoutCall20>(taken[20]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[21]) {
      int handled = 0;
      CuteQHBoxLayoutCall21 call = reinterpret_cast<CuteQHBoxLayoutCall21>(taken[21]);
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
      CuteQHBoxLayoutCall22 call = reinterpret_cast<CuteQHBoxLayoutCall22>(taken[22]);
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
      CuteQHBoxLayoutCall23 call = reinterpret_cast<CuteQHBoxLayoutCall23>(taken[23]);
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
      CuteQHBoxLayoutCall24 call = reinterpret_cast<CuteQHBoxLayoutCall24>(taken[24]);
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
      CuteQHBoxLayoutCall25 call = reinterpret_cast<CuteQHBoxLayoutCall25>(taken[25]);
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
      CuteQHBoxLayoutCall26 call = reinterpret_cast<CuteQHBoxLayoutCall26>(taken[26]);
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
      CuteQHBoxLayoutCall27 call = reinterpret_cast<CuteQHBoxLayoutCall27>(taken[27]);
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
      CuteQHBoxLayoutCall28 call = reinterpret_cast<CuteQHBoxLayoutCall28>(taken[28]);
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
      CuteQHBoxLayoutCall29 call = reinterpret_cast<CuteQHBoxLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQHBoxLayoutCall30 call = reinterpret_cast<CuteQHBoxLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QHBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHBoxLayout10metaObjectEv(
    const QHBoxLayout *self) {
  return self->metaObject();
}

//  QString QHBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHBoxLayout::tr(s, c, n));
}

//  QHBoxLayout::QHBoxLayout()
extern "C" Q_DECL_EXPORT
QHBoxLayout *ritual_ZN11QHBoxLayoutC1Ev() {
  return new CuteQHBoxLayout();
}

//  QHBoxLayout::QHBoxLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QHBoxLayout *ritual_ZN11QHBoxLayoutC1EP7QWidget(QWidget *parent) {
  return new CuteQHBoxLayout(parent);
}

//  QHBoxLayout::~QHBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHBoxLayoutD1Ev(QHBoxLayout *self) {
  delete self;
}

//  a Python function taken by a CuteQHBoxLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHBoxLayout(
    QHBoxLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHBoxLayout *>(self)->take(key, call);
}
