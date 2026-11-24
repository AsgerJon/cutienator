//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatforminputcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatforminputcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformInputContext that Python can take functions over in. Every QPlatformInputContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformInputContextCall0)(const void *, int *);
typedef bool (*CuteQPlatformInputContextCall1)(const void *, int, int *);
typedef void (*CuteQPlatformInputContextCall2)(const void *, int *);
typedef void (*CuteQPlatformInputContextCall3)(const void *, int *);
typedef void (*CuteQPlatformInputContextCall4)(const void *, int, int *);
typedef void (*CuteQPlatformInputContextCall5)(const void *, int, int, int *);
typedef bool (*CuteQPlatformInputContextCall6)(const void *, const QEvent *, int *);
typedef const QRectF * (*CuteQPlatformInputContextCall7)(const void *, int *);
typedef bool (*CuteQPlatformInputContextCall8)(const void *, int *);
typedef void (*CuteQPlatformInputContextCall9)(const void *, int *);
typedef void (*CuteQPlatformInputContextCall10)(const void *, int *);
typedef bool (*CuteQPlatformInputContextCall11)(const void *, int *);
typedef const QLocale * (*CuteQPlatformInputContextCall12)(const void *, int *);
typedef int (*CuteQPlatformInputContextCall13)(const void *, int *);
typedef void (*CuteQPlatformInputContextCall14)(const void *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformInputContextCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformInputContextCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformInputContextCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformInputContextCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformInputContextCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformInputContextCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformInputContextCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformInputContext : public QPlatformInputContext {
public:
  using QPlatformInputContext::QPlatformInputContext;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext6commitEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6ActionEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext11filterEventEPK6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext12keyboardRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext11isAnimatingEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14showInputPanelEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14hideInputPanelEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext19isInputPanelVisibleEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext6localeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext14inputDirectionEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14setFocusObjectEP7QObject")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QPlatformInputContext::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformInputContextCall0 call = reinterpret_cast<CuteQPlatformInputContextCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::isValid();
  }

  //  bool QPlatformInputContext::hasCapability(Capability capability)
  //      const
  bool hasCapability(
      QPlatformInputContext::Capability capability) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformInputContextCall1 call = reinterpret_cast<CuteQPlatformInputContextCall1>(taken[1]);
      bool given = call(this, static_cast<int>(capability), &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::hasCapability(capability);
  }

  //  void QPlatformInputContext::reset()
  void reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformInputContextCall2 call = reinterpret_cast<CuteQPlatformInputContextCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformInputContext::reset();
  }

  //  void QPlatformInputContext::commit()
  void commit() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformInputContextCall3 call = reinterpret_cast<CuteQPlatformInputContextCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformInputContext::commit();
  }

  //  void QPlatformInputContext::update(Qt::InputMethodQueries a0)
  void update(Qt::InputMethodQueries a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformInputContextCall4 call = reinterpret_cast<CuteQPlatformInputContextCall4>(taken[4]);
      call(this, static_cast<int>(a0.toInt()), &handled);
      if (handled) return;
    }
    QPlatformInputContext::update(a0);
  }

  //  void QPlatformInputContext::invokeAction(QInputMethod::Action a0, int
  //      cursorPosition)
  void invokeAction(QInputMethod::Action a0, int cursorPosition) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformInputContextCall5 call = reinterpret_cast<CuteQPlatformInputContextCall5>(taken[5]);
      call(this, static_cast<int>(a0), cursorPosition, &handled);
      if (handled) return;
    }
    QPlatformInputContext::invokeAction(a0, cursorPosition);
  }

  //  bool QPlatformInputContext::filterEvent(const QEvent *event)
  bool filterEvent(const QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformInputContextCall6 call = reinterpret_cast<CuteQPlatformInputContextCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::filterEvent(event);
  }

  //  QRectF QPlatformInputContext::keyboardRect() const
  QRectF keyboardRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformInputContextCall7 call = reinterpret_cast<CuteQPlatformInputContextCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformInputContext::keyboardRect();
  }

  //  bool QPlatformInputContext::isAnimating() const
  bool isAnimating() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformInputContextCall8 call = reinterpret_cast<CuteQPlatformInputContextCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::isAnimating();
  }

  //  void QPlatformInputContext::showInputPanel()
  void showInputPanel() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformInputContextCall9 call = reinterpret_cast<CuteQPlatformInputContextCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformInputContext::showInputPanel();
  }

  //  void QPlatformInputContext::hideInputPanel()
  void hideInputPanel() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformInputContextCall10 call = reinterpret_cast<CuteQPlatformInputContextCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformInputContext::hideInputPanel();
  }

  //  bool QPlatformInputContext::isInputPanelVisible() const
  bool isInputPanelVisible() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformInputContextCall11 call = reinterpret_cast<CuteQPlatformInputContextCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::isInputPanelVisible();
  }

  //  QLocale QPlatformInputContext::locale() const
  QLocale locale() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformInputContextCall12 call = reinterpret_cast<CuteQPlatformInputContextCall12>(taken[12]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformInputContext::locale();
  }

  //  Qt::LayoutDirection QPlatformInputContext::inputDirection() const
  Qt::LayoutDirection inputDirection() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformInputContextCall13 call = reinterpret_cast<CuteQPlatformInputContextCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::LayoutDirection>(given);
    }
    return QPlatformInputContext::inputDirection();
  }

  //  void QPlatformInputContext::setFocusObject(QObject *object)
  void setFocusObject(QObject *object) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformInputContextCall14 call = reinterpret_cast<CuteQPlatformInputContextCall14>(taken[14]);
      call(this, object, &handled);
      if (handled) return;
    }
    QPlatformInputContext::setFocusObject(object);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformInputContextCall15 call = reinterpret_cast<CuteQPlatformInputContextCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformInputContextCall16 call = reinterpret_cast<CuteQPlatformInputContextCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformInputContextCall17 call = reinterpret_cast<CuteQPlatformInputContextCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformInputContextCall18 call = reinterpret_cast<CuteQPlatformInputContextCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformInputContextCall19 call = reinterpret_cast<CuteQPlatformInputContextCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformInputContextCall20 call = reinterpret_cast<CuteQPlatformInputContextCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformInputContextCall21 call = reinterpret_cast<CuteQPlatformInputContextCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformInputContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlatformInputContext10metaObjectEv(
    const QPlatformInputContext *self) {
  return self->metaObject();
}

//  QString QPlatformInputContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPlatformInputContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformInputContext::tr(s, c, n));
}

//  QPlatformInputContextPrivate *QPlatformInputContext::d_func()
extern "C" Q_DECL_EXPORT
QPlatformInputContextPrivate *ritual_ZN21QPlatformInputContext6d_funcEv(
    QPlatformInputContext *self) {
  return self->d_func();
}

//  const QPlatformInputContextPrivate *QPlatformInputContext::d_func() const
extern "C" Q_DECL_EXPORT
const QPlatformInputContextPrivate *ritual_ZNK21QPlatformInputContext6d_funcEv(
    const QPlatformInputContext *self) {
  return self->d_func();
}

//  QPlatformInputContext::QPlatformInputContext()
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZN21QPlatformInputContextC1Ev() {
  return new CuteQPlatformInputContext();
}

//  QPlatformInputContext::~QPlatformInputContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContextD1Ev(QPlatformInputContext *self) {
  delete self;
}

//  bool QPlatformInputContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformInputContext7isValidEv(
    const QPlatformInputContext *self) {
  return self->isValid();
}

//  bool QPlatformInputContext::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE(
    const QPlatformInputContext *self,
    QPlatformInputContext::Capability capability) {
  return self->hasCapability(capability);
}

//  void QPlatformInputContext::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext5resetEv(QPlatformInputContext *self) {
  self->reset();
}

//  void QPlatformInputContext::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext6commitEv(QPlatformInputContext *self) {
  self->commit();
}

//  void QPlatformInputContext::update(Qt::InputMethodQueries a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QPlatformInputContext *self,
    int a0) {
  self->update(QFlags<Qt::InputMethodQuery>::fromInt(a0));
}

//  void QPlatformInputContext::invokeAction(QInputMethod::Action a0, int
//      cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6ActionEi(
    QPlatformInputContext *self,
    QInputMethod::Action a0,
    int cursorPosition) {
  self->invokeAction(a0, cursorPosition);
}

//  bool QPlatformInputContext::filterEvent(const QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPlatformInputContext11filterEventEPK6QEvent(
    QPlatformInputContext *self,
    const QEvent *event) {
  return self->filterEvent(event);
}

//  QRectF QPlatformInputContext::keyboardRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QPlatformInputContext12keyboardRectEv(
    const QPlatformInputContext *self) {
  return new QRectF(self->keyboardRect());
}

//  void QPlatformInputContext::emitKeyboardRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext23emitKeyboardRectChangedEv(
    QPlatformInputContext *self) {
  self->emitKeyboardRectChanged();
}

//  bool QPlatformInputContext::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformInputContext11isAnimatingEv(
    const QPlatformInputContext *self) {
  return self->isAnimating();
}

//  void QPlatformInputContext::emitAnimatingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext20emitAnimatingChangedEv(
    QPlatformInputContext *self) {
  self->emitAnimatingChanged();
}

//  void QPlatformInputContext::showInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext14showInputPanelEv(
    QPlatformInputContext *self) {
  self->showInputPanel();
}

//  void QPlatformInputContext::hideInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext14hideInputPanelEv(
    QPlatformInputContext *self) {
  self->hideInputPanel();
}

//  bool QPlatformInputContext::isInputPanelVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformInputContext19isInputPanelVisibleEv(
    const QPlatformInputContext *self) {
  return self->isInputPanelVisible();
}

//  void QPlatformInputContext::emitInputPanelVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext28emitInputPanelVisibleChangedEv(
    QPlatformInputContext *self) {
  self->emitInputPanelVisibleChanged();
}

//  QLocale QPlatformInputContext::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK21QPlatformInputContext6localeEv(
    const QPlatformInputContext *self) {
  return new QLocale(self->locale());
}

//  void QPlatformInputContext::emitLocaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext17emitLocaleChangedEv(
    QPlatformInputContext *self) {
  self->emitLocaleChanged();
}

//  Qt::LayoutDirection QPlatformInputContext::inputDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK21QPlatformInputContext14inputDirectionEv(
    const QPlatformInputContext *self) {
  return self->inputDirection();
}

//  void QPlatformInputContext::emitInputDirectionChanged(Qt::LayoutDirection
//      newDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext25emitInputDirectionChangedEN2Qt15LayoutDirectionE(
    QPlatformInputContext *self,
    Qt::LayoutDirection newDirection) {
  self->emitInputDirectionChanged(newDirection);
}

//  void QPlatformInputContext::setFocusObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext14setFocusObjectEP7QObject(
    QPlatformInputContext *self,
    QObject *object) {
  self->setFocusObject(object);
}

//  bool QPlatformInputContext::inputMethodAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformInputContext19inputMethodAcceptedEv(
    const QPlatformInputContext *self) {
  return self->inputMethodAccepted();
}

//  void QPlatformInputContext::setSelectionOnFocusObject(const QPointF
//      &anchorPos, const QPointF &cursorPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformInputContext25setSelectionOnFocusObjectERK7QPointFS2_(
    const QPointF *anchorPos,
    const QPointF *cursorPos) {
  QPlatformInputContext::setSelectionOnFocusObject(*anchorPos, *cursorPos);
}

//  QVariant QPlatformInputContext::queryFocusObject(Qt::InputMethodQuery
//      query, QPointF position)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN21QPlatformInputContext16queryFocusObjectEN2Qt16InputMethodQueryE7QPointF(
    Qt::InputMethodQuery query,
    const QPointF *position) {
  return new QVariant(
      QPlatformInputContext::queryFocusObject(
          query,
          *position));
}

//  QRectF QPlatformInputContext::inputItemRectangle()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlatformInputContext18inputItemRectangleEv() {
  return new QRectF(QPlatformInputContext::inputItemRectangle());
}

//  QRectF QPlatformInputContext::inputItemClipRectangle()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlatformInputContext22inputItemClipRectangleEv() {
  return new QRectF(QPlatformInputContext::inputItemClipRectangle());
}

//  QRectF QPlatformInputContext::cursorRectangle()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlatformInputContext15cursorRectangleEv() {
  return new QRectF(QPlatformInputContext::cursorRectangle());
}

//  QRectF QPlatformInputContext::anchorRectangle()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlatformInputContext15anchorRectangleEv() {
  return new QRectF(QPlatformInputContext::anchorRectangle());
}

//  QRectF QPlatformInputContext::keyboardRectangle()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlatformInputContext17keyboardRectangleEv() {
  return new QRectF(QPlatformInputContext::keyboardRectangle());
}

//  a Python function taken by a CuteQPlatformInputContext, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformInputContext(
    QPlatformInputContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformInputContext *>(self)->take(key, call);
}

//  bool QPlatformInputContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformInputContext7isValidEv(
    const QPlatformInputContext *self) {
  return self->QPlatformInputContext::isValid();
}

//  bool QPlatformInputContext::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE(
    const QPlatformInputContext *self,
    QPlatformInputContext::Capability capability) {
  return self->QPlatformInputContext::hasCapability(capability);
}

//  void QPlatformInputContext::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext5resetEv(
    QPlatformInputContext *self) {
  self->QPlatformInputContext::reset();
}

//  void QPlatformInputContext::commit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext6commitEv(
    QPlatformInputContext *self) {
  self->QPlatformInputContext::commit();
}

//  void QPlatformInputContext::update(Qt::InputMethodQueries a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QPlatformInputContext *self,
    int a0) {
  self->QPlatformInputContext::update(
      QFlags<Qt::InputMethodQuery>::fromInt(a0));
}

//  void QPlatformInputContext::invokeAction(QInputMethod::Action a0, int
//      cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6ActionEi(
    QPlatformInputContext *self,
    QInputMethod::Action a0,
    int cursorPosition) {
  self->QPlatformInputContext::invokeAction(a0, cursorPosition);
}

//  bool QPlatformInputContext::filterEvent(const QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QPlatformInputContext11filterEventEPK6QEvent(
    QPlatformInputContext *self,
    const QEvent *event) {
  return self->QPlatformInputContext::filterEvent(event);
}

//  QRectF QPlatformInputContext::keyboardRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK21QPlatformInputContext12keyboardRectEv(
    const QPlatformInputContext *self) {
  return new QRectF(self->QPlatformInputContext::keyboardRect());
}

//  bool QPlatformInputContext::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformInputContext11isAnimatingEv(
    const QPlatformInputContext *self) {
  return self->QPlatformInputContext::isAnimating();
}

//  void QPlatformInputContext::showInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext14showInputPanelEv(
    QPlatformInputContext *self) {
  self->QPlatformInputContext::showInputPanel();
}

//  void QPlatformInputContext::hideInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext14hideInputPanelEv(
    QPlatformInputContext *self) {
  self->QPlatformInputContext::hideInputPanel();
}

//  bool QPlatformInputContext::isInputPanelVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformInputContext19isInputPanelVisibleEv(
    const QPlatformInputContext *self) {
  return self->QPlatformInputContext::isInputPanelVisible();
}

//  QLocale QPlatformInputContext::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_own_ZNK21QPlatformInputContext6localeEv(
    const QPlatformInputContext *self) {
  return new QLocale(self->QPlatformInputContext::locale());
}

//  Qt::LayoutDirection QPlatformInputContext::inputDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_own_ZNK21QPlatformInputContext14inputDirectionEv(
    const QPlatformInputContext *self) {
  return self->QPlatformInputContext::inputDirection();
}

//  void QPlatformInputContext::setFocusObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformInputContext14setFocusObjectEP7QObject(
    QPlatformInputContext *self,
    QObject *object) {
  self->QPlatformInputContext::setFocusObject(object);
}
