//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitreader_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: the ritual of
//  typeAsControlType() is taken out, for Qt's library does not offer
//  it (it is declared and defined only in a debug build of Qt).
//  Kept as it is when the generator runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQStyleKitReader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQStyleKitReader : QQStyleKitReader {
  using QQStyleKitReader::classBegin;
  using QQStyleKitReader::componentComplete;
};

//  A QQStyleKitReader that Python can take functions over in. Every QQStyleKitReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQStyleKitReaderCall0)(const void *, int *);
typedef void (*CuteQQStyleKitReaderCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitReaderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitReaderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitReaderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitReaderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitReaderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitReaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitReaderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitReader : public QQStyleKitReader {
public:
  using QQStyleKitReader::QQStyleKitReader;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQStyleKitReader::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQStyleKitReaderCall0 call = reinterpret_cast<CuteQQStyleKitReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQStyleKitReader::classBegin();
  }

  //  void QQStyleKitReader::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQStyleKitReaderCall1 call = reinterpret_cast<CuteQQStyleKitReaderCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQStyleKitReader::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQStyleKitReaderCall2 call = reinterpret_cast<CuteQQStyleKitReaderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQStyleKitReaderCall3 call = reinterpret_cast<CuteQQStyleKitReaderCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQStyleKitReaderCall4 call = reinterpret_cast<CuteQQStyleKitReaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQStyleKitReaderCall5 call = reinterpret_cast<CuteQQStyleKitReaderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQStyleKitReaderCall6 call = reinterpret_cast<CuteQQStyleKitReaderCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQStyleKitReaderCall7 call = reinterpret_cast<CuteQQStyleKitReaderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQStyleKitReaderCall8 call = reinterpret_cast<CuteQQStyleKitReaderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitReader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQStyleKitReader10metaObjectEv(
    const QQStyleKitReader *self) {
  return self->metaObject();
}

//  void *QQStyleKitReader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQStyleKitReader11qt_metacastEPKc(
    QQStyleKitReader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QQStyleKitReader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQStyleKitReader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitReader::tr(s, c, n));
}

//  QQStyleKitReader::QQStyleKitReader(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitReader *ritual_ZN16QQStyleKitReaderC1EP7QObject(QObject *parent) {
  return new CuteQQStyleKitReader(parent);
}

//  QQStyleKitReader::~QQStyleKitReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReaderD1Ev(QQStyleKitReader *self) {
  delete self;
}

//  QQStyleKitExtendableControlType QQStyleKitReader::controlType() const
extern "C" Q_DECL_EXPORT
QQStyleKitExtendableControlType ritual_ZNK16QQStyleKitReader11controlTypeEv(
    const QQStyleKitReader *self) {
  return self->controlType();
}

//  void QQStyleKitReader::setControlType(QQStyleKitExtendableControlType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader14setControlTypeEj(
    QQStyleKitReader *self,
    QQStyleKitExtendableControlType type) {
  self->setControlType(type);
}

//  bool QQStyleKitReader::hovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader7hoveredEv(const QQStyleKitReader *self) {
  return self->hovered();
}

//  void QQStyleKitReader::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setHoveredEb(
    QQStyleKitReader *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  bool QQStyleKitReader::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader7enabledEv(const QQStyleKitReader *self) {
  return self->enabled();
}

//  void QQStyleKitReader::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setEnabledEb(
    QQStyleKitReader *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQStyleKitReader::focused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader7focusedEv(const QQStyleKitReader *self) {
  return self->focused();
}

//  void QQStyleKitReader::setFocused(bool focused)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setFocusedEb(
    QQStyleKitReader *self,
    bool focused) {
  self->setFocused(focused);
}

//  bool QQStyleKitReader::checked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader7checkedEv(const QQStyleKitReader *self) {
  return self->checked();
}

//  void QQStyleKitReader::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setCheckedEb(
    QQStyleKitReader *self,
    bool checked) {
  self->setChecked(checked);
}

//  bool QQStyleKitReader::pressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader7pressedEv(const QQStyleKitReader *self) {
  return self->pressed();
}

//  void QQStyleKitReader::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setPressedEb(
    QQStyleKitReader *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  QQuickPalette *QQStyleKitReader::palette() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK16QQStyleKitReader7paletteEv(
    const QQStyleKitReader *self) {
  return self->palette();
}

//  void QQStyleKitReader::setPalette(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10setPaletteEP13QQuickPalette(
    QQStyleKitReader *self,
    QQuickPalette *palette) {
  self->setPalette(palette);
}

//  QPalette QQStyleKitReader::effectivePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK16QQStyleKitReader16effectivePaletteEv(
    const QQStyleKitReader *self) {
  return new QPalette(self->effectivePalette());
}

//  bool QQStyleKitReader::vertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader8verticalEv(const QQStyleKitReader *self) {
  return self->vertical();
}

//  void QQStyleKitReader::setVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader11setVerticalEb(
    QQStyleKitReader *self,
    bool vertical) {
  self->setVertical(vertical);
}

//  bool QQStyleKitReader::highlighted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader11highlightedEv(
    const QQStyleKitReader *self) {
  return self->highlighted();
}

//  void QQStyleKitReader::setHighlighted(bool highlighted)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader14setHighlightedEb(
    QQStyleKitReader *self,
    bool highlighted) {
  self->setHighlighted(highlighted);
}

//  QQStyleKitStyle *QQStyleKitReader::explicitStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK16QQStyleKitReader13explicitStyleEv(
    const QQStyleKitReader *self) {
  return self->explicitStyle();
}

//  void QQStyleKitReader::setExplicitStyle(QQStyleKitStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader16setExplicitStyleEP15QQStyleKitStyle(
    QQStyleKitReader *self,
    QQStyleKitStyle *style) {
  self->setExplicitStyle(style);
}

//  QFont QQStyleKitReader::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QQStyleKitReader4fontEv(const QQStyleKitReader *self) {
  return new QFont(self->font());
}

//  QQStyleKitControlProperties *QQStyleKitReader::global() const
extern "C" Q_DECL_EXPORT
QQStyleKitControlProperties *ritual_ZNK16QQStyleKitReader6globalEv(
    const QQStyleKitReader *self) {
  return self->global();
}

//  QVariant QQStyleKitReader::readStyleProperty(PropertyStorageId key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQStyleKitReader17readStylePropertyEj(
    const QQStyleKitReader *self,
    PropertyStorageId key) {
  return new QVariant(self->readStyleProperty(key));
}

//  void QQStyleKitReader::writeStyleProperty(PropertyStorageId key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader18writeStylePropertyEjRK8QVariant(
    QQStyleKitReader *self,
    PropertyStorageId key,
    const QVariant *value) {
  self->writeStyleProperty(key, *value);
}

//  void QQStyleKitReader::clearLocalStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader17clearLocalStorageEv(
    QQStyleKitReader *self) {
  self->clearLocalStorage();
}

//  QQSK::State QQStyleKitReader::controlState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQStyleKitReader12controlStateEv(
    const QQStyleKitReader *self) {
  return static_cast<int>(self->controlState().toInt());
}

//  void
//      QQStyleKitReader::setControlTypeAndState(QQStyleKitExtendableControlT
//      ype controlType, QQSK::State flags, bool applyStateChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader22setControlTypeAndStateEj6QFlagsIN4QQSK9StateFlagEEb(
    QQStyleKitReader *self,
    QQStyleKitExtendableControlType controlType,
    int flags,
    bool applyStateChange) {
  self->setControlTypeAndState(
      controlType,
      QFlags<QQSK::StateFlag>::fromInt(flags),
      applyStateChange);
}

//  QObject *QQStyleKitReader::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQStyleKitReader6targetEv(
    const QQStyleKitReader *self) {
  return self->target();
}

//  void QQStyleKitReader::setTarget(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader9setTargetEP7QObject(
    QQStyleKitReader *self,
    QObject *target) {
  self->setTarget(target);
}

//  void QQStyleKitReader::setCompleted(bool completed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader12setCompletedEb(
    QQStyleKitReader *self,
    bool completed) {
  self->setCompleted(completed);
}

//  bool QQStyleKitReader::transitionsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader18transitionsEnabledEv(
    const QQStyleKitReader *self) {
  return self->transitionsEnabled();
}

//  void QQStyleKitReader::setTransitionsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader21setTransitionsEnabledEb(
    QQStyleKitReader *self,
    bool enabled) {
  self->setTransitionsEnabled(enabled);
}

//  void QQStyleKitReader::resetReadersForStyle(const QQStyleKitStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader20resetReadersForStyleEPK15QQStyleKitStyle(
    const QQStyleKitStyle *style) {
  QQStyleKitReader::resetReadersForStyle(style);
}

//  void QQStyleKitReader::onPaletteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader16onPaletteChangedEv(
    QQStyleKitReader *self) {
  self->onPaletteChanged();
}

//  void QQStyleKitReader::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader10classBeginEv(QQStyleKitReader *self) {
  self->classBegin();
}

//  void QQStyleKitReader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader17componentCompleteEv(
    QQStyleKitReader *self) {
  self->componentComplete();
}

//  void QQStyleKitReader::updateControl(bool applyStateChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader13updateControlEb(
    QQStyleKitReader *self,
    bool applyStateChange) {
  self->updateControl(applyStateChange);
}

//  void QQStyleKitReader::populateLocalStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader20populateLocalStorageEv(
    QQStyleKitReader *self) {
  self->populateLocalStorage();
}

//  bool QQStyleKitReader::dontEmitChangedSignals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitReader22dontEmitChangedSignalsEv(
    const QQStyleKitReader *self) {
  return self->dontEmitChangedSignals();
}

//  QQuickStateGroup *QQStyleKitReader::stateGroup()
extern "C" Q_DECL_EXPORT
QQuickStateGroup *ritual_ZN16QQStyleKitReader10stateGroupEv(
    QQStyleKitReader *self) {
  return self->stateGroup();
}

//  QQmlComponent *QQStyleKitReader::createControlChangesComponent() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK16QQStyleKitReader29createControlChangesComponentEv(
    const QQStyleKitReader *self) {
  return self->createControlChangesComponent();
}

//  QQmlComponent *QQStyleKitReader::createDelegateChangesComponent(const
//      QString &delegateName) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK16QQStyleKitReader30createDelegateChangesComponentERK7QString(
    const QQStyleKitReader *self,
    const QString *delegateName) {
  return self->createDelegateChangesComponent(*delegateName);
}

//  void QQStyleKitReader::instantiatePropertyChanges(QQmlComponent *comp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader26instantiatePropertyChangesEP13QQmlComponent(
    QQStyleKitReader *self,
    QQmlComponent *comp) {
  self->instantiatePropertyChanges(comp);
}

//  void QQStyleKitReader::maybeTrackDelegates()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitReader19maybeTrackDelegatesEv(
    QQStyleKitReader *self) {
  self->maybeTrackDelegates();
}

//  bool QQStyleKitReader::rebuildEffectivePalette()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQStyleKitReader23rebuildEffectivePaletteEv(
    QQStyleKitReader *self) {
  return self->rebuildEffectivePalette();
}

//  bool QQStyleKitReader::rebuildEffectiveFont()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQStyleKitReader20rebuildEffectiveFontEv(
    QQStyleKitReader *self) {
  return self->rebuildEffectiveFont();
}

//  QQStyleKitReader as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQStyleKitReader_QQmlParserStatus(
    QQStyleKitReader *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQStyleKitReader, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitReader(
    QQStyleKitReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitReader *>(self)->take(key, call);
}

//  void QQStyleKitReader::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQStyleKitReader10classBeginEv(QQStyleKitReader *self) {
  static_cast<OwnQQStyleKitReader *>(self)->OwnQQStyleKitReader::classBegin();
}

//  void QQStyleKitReader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQStyleKitReader17componentCompleteEv(
    QQStyleKitReader *self) {
  static_cast<OwnQQStyleKitReader *>(self)->OwnQQStyleKitReader::componentComplete();
}
