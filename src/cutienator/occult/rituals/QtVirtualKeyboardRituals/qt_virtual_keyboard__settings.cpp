//  Written by hand on 2026-11-25 from
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/settings_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Left out: 'availableLocales', 'setAvailableLocales',
//  'activeLocales' and 'setActiveLocales', which take or give a
//  'QStringList'; the destructor, which Qt does not declare. The
//  constructor is private, and is written, as private members may be
//  named.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/settings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/qurl.h>

//  A QtVirtualKeyboard::Settings that Python can take functions over in. Every QtVirtualKeyboard::Settings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_SettingsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_SettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_SettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_SettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_SettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_SettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_SettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_Settings : public QtVirtualKeyboard::Settings {
public:
  using QtVirtualKeyboard::Settings::Settings;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_SettingsCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_SettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::Settings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard8Settings10metaObjectEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::Settings::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard8Settings2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::Settings::tr(s, c, n));
}

//  QtVirtualKeyboard::Settings::Settings(QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::Settings *ritual_ZN17QtVirtualKeyboard8SettingsC1EP7QObject(
    QObject *parent) {
  return new CuteQtVirtualKeyboard_Settings(parent);
}

//  static QtVirtualKeyboard::Settings
//      *QtVirtualKeyboard::Settings::instance()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::Settings *ritual_ZN17QtVirtualKeyboard8Settings8instanceEv() {
  return QtVirtualKeyboard::Settings::instance();
}

//  QString QtVirtualKeyboard::Settings::style() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard8Settings5styleEv(
    const QtVirtualKeyboard::Settings *self) {
  return new QString(self->style());
}

//  void QtVirtualKeyboard::Settings::setStyle(const QString &style)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings8setStyleERK7QString(
    QtVirtualKeyboard::Settings *self,
    const QString *style) {
  self->setStyle(*style);
}

//  QString QtVirtualKeyboard::Settings::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard8Settings9styleNameEv(
    const QtVirtualKeyboard::Settings *self) {
  return new QString(self->styleName());
}

//  void QtVirtualKeyboard::Settings::setStyleName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings12setStyleNameERK7QString(
    QtVirtualKeyboard::Settings *self,
    const QString *name) {
  self->setStyleName(*name);
}

//  void QtVirtualKeyboard::Settings::resetStyleName()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings14resetStyleNameEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetStyleName();
}

//  QString QtVirtualKeyboard::Settings::locale() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard8Settings6localeEv(
    const QtVirtualKeyboard::Settings *self) {
  return new QString(self->locale());
}

//  void QtVirtualKeyboard::Settings::setLocale(const QString &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings9setLocaleERK7QString(
    QtVirtualKeyboard::Settings *self,
    const QString *locale) {
  self->setLocale(*locale);
}

//  void QtVirtualKeyboard::Settings::resetLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings11resetLocaleEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetLocale();
}

//  void QtVirtualKeyboard::Settings::resetActiveLocales()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings18resetActiveLocalesEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetActiveLocales();
}

//  QUrl QtVirtualKeyboard::Settings::layoutPath() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QtVirtualKeyboard8Settings10layoutPathEv(
    const QtVirtualKeyboard::Settings *self) {
  return new QUrl(self->layoutPath());
}

//  void QtVirtualKeyboard::Settings::setLayoutPath(const QUrl &layoutPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings13setLayoutPathERK4QUrl(
    QtVirtualKeyboard::Settings *self,
    const QUrl *layoutPath) {
  self->setLayoutPath(*layoutPath);
}

//  void QtVirtualKeyboard::Settings::resetLayoutPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings15resetLayoutPathEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetLayoutPath();
}

//  int QtVirtualKeyboard::Settings::wclAutoHideDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard8Settings16wclAutoHideDelayEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->wclAutoHideDelay();
}

//  void QtVirtualKeyboard::Settings::setWclAutoHideDelay(int
//      wclAutoHideDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19setWclAutoHideDelayEi(
    QtVirtualKeyboard::Settings *self,
    int wclAutoHideDelay) {
  self->setWclAutoHideDelay(wclAutoHideDelay);
}

//  void QtVirtualKeyboard::Settings::resetWclAutoHideDelay()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21resetWclAutoHideDelayEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetWclAutoHideDelay();
}

//  bool QtVirtualKeyboard::Settings::wclAlwaysVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings16wclAlwaysVisibleEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->wclAlwaysVisible();
}

//  void QtVirtualKeyboard::Settings::setWclAlwaysVisible(bool
//      wclAlwaysVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19setWclAlwaysVisibleEb(
    QtVirtualKeyboard::Settings *self,
    bool wclAlwaysVisible) {
  self->setWclAlwaysVisible(wclAlwaysVisible);
}

//  void QtVirtualKeyboard::Settings::resetWclAlwaysVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21resetWclAlwaysVisibleEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetWclAlwaysVisible();
}

//  bool QtVirtualKeyboard::Settings::wclAutoCommitWord() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings17wclAutoCommitWordEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->wclAutoCommitWord();
}

//  void QtVirtualKeyboard::Settings::setWclAutoCommitWord(bool
//      wclAutoCommitWord)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings20setWclAutoCommitWordEb(
    QtVirtualKeyboard::Settings *self,
    bool wclAutoCommitWord) {
  self->setWclAutoCommitWord(wclAutoCommitWord);
}

//  void QtVirtualKeyboard::Settings::resetWclAutoCommitWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings22resetWclAutoCommitWordEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetWclAutoCommitWord();
}

//  bool QtVirtualKeyboard::Settings::fullScreenMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings14fullScreenModeEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->fullScreenMode();
}

//  void QtVirtualKeyboard::Settings::setFullScreenMode(bool fullScreenMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings17setFullScreenModeEb(
    QtVirtualKeyboard::Settings *self,
    bool fullScreenMode) {
  self->setFullScreenMode(fullScreenMode);
}

//  void QtVirtualKeyboard::Settings::resetFullScreenMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19resetFullScreenModeEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetFullScreenMode();
}

//  QString QtVirtualKeyboard::Settings::userDataPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard8Settings12userDataPathEv(
    const QtVirtualKeyboard::Settings *self) {
  return new QString(self->userDataPath());
}

//  void QtVirtualKeyboard::Settings::setUserDataPath(const QString
//      &userDataPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings15setUserDataPathERK7QString(
    QtVirtualKeyboard::Settings *self,
    const QString *userDataPath) {
  self->setUserDataPath(*userDataPath);
}

//  void QtVirtualKeyboard::Settings::resetUserDataPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings17resetUserDataPathEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetUserDataPath();
}

//  int QtVirtualKeyboard::Settings::hwrTimeoutForAlphabetic() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard8Settings23hwrTimeoutForAlphabeticEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->hwrTimeoutForAlphabetic();
}

//  void QtVirtualKeyboard::Settings::setHwrTimeoutForAlphabetic(int
//      hwrTimeoutForAlphabetic)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings26setHwrTimeoutForAlphabeticEi(
    QtVirtualKeyboard::Settings *self,
    int hwrTimeoutForAlphabetic) {
  self->setHwrTimeoutForAlphabetic(hwrTimeoutForAlphabetic);
}

//  void QtVirtualKeyboard::Settings::resetHwrTimeoutForAlphabetic()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings28resetHwrTimeoutForAlphabeticEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetHwrTimeoutForAlphabetic();
}

//  int QtVirtualKeyboard::Settings::hwrTimeoutForCjk() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard8Settings16hwrTimeoutForCjkEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->hwrTimeoutForCjk();
}

//  void QtVirtualKeyboard::Settings::setHwrTimeoutForCjk(int
//      hwrTimeoutForCjk)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19setHwrTimeoutForCjkEi(
    QtVirtualKeyboard::Settings *self,
    int hwrTimeoutForCjk) {
  self->setHwrTimeoutForCjk(hwrTimeoutForCjk);
}

//  void QtVirtualKeyboard::Settings::resetHwrTimeoutForCjk()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21resetHwrTimeoutForCjkEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetHwrTimeoutForCjk();
}

//  Qt::InputMethodHints QtVirtualKeyboard::Settings::inputMethodHints()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard8Settings16inputMethodHintsEv(
    const QtVirtualKeyboard::Settings *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QtVirtualKeyboard::Settings::setInputMethodHints(const
//      Qt::InputMethodHints &inputMethodHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19setInputMethodHintsERK6QFlagsIN2Qt15InputMethodHintEE(
    QtVirtualKeyboard::Settings *self,
    int inputMethodHints) {
  self->setInputMethodHints(Qt::InputMethodHints::fromInt(inputMethodHints));
}

//  void QtVirtualKeyboard::Settings::resetInputMethodHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21resetInputMethodHintsEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetInputMethodHints();
}

//  bool QtVirtualKeyboard::Settings::isHandwritingModeDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings25isHandwritingModeDisabledEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->isHandwritingModeDisabled();
}

//  void QtVirtualKeyboard::Settings::setHandwritingModeDisabled(bool
//      handwritingModeDisabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings26setHandwritingModeDisabledEb(
    QtVirtualKeyboard::Settings *self,
    bool handwritingModeDisabled) {
  self->setHandwritingModeDisabled(handwritingModeDisabled);
}

//  void QtVirtualKeyboard::Settings::resetHandwritingModeDisabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings28resetHandwritingModeDisabledEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetHandwritingModeDisabled();
}

//  bool QtVirtualKeyboard::Settings::isDefaultInputMethodDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings28isDefaultInputMethodDisabledEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->isDefaultInputMethodDisabled();
}

//  void QtVirtualKeyboard::Settings::setDefaultInputMethodDisabled(bool
//      defaultInputMethodDisabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings29setDefaultInputMethodDisabledEb(
    QtVirtualKeyboard::Settings *self,
    bool defaultInputMethodDisabled) {
  self->setDefaultInputMethodDisabled(defaultInputMethodDisabled);
}

//  void QtVirtualKeyboard::Settings::resetDefaultInputMethodDisabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings31resetDefaultInputMethodDisabledEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetDefaultInputMethodDisabled();
}

//  bool QtVirtualKeyboard::Settings::isDefaultDictionaryDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings27isDefaultDictionaryDisabledEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->isDefaultDictionaryDisabled();
}

//  void QtVirtualKeyboard::Settings::setDefaultDictionaryDisabled(bool
//      defaultDictionaryDisabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings28setDefaultDictionaryDisabledEb(
    QtVirtualKeyboard::Settings *self,
    bool defaultDictionaryDisabled) {
  self->setDefaultDictionaryDisabled(defaultDictionaryDisabled);
}

//  void QtVirtualKeyboard::Settings::resetDefaultDictionaryDisabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings30resetDefaultDictionaryDisabledEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetDefaultDictionaryDisabled();
}

//  QtVirtualKeyboard::KeyboardFunctionKeys
//      QtVirtualKeyboard::Settings::visibleFunctionKeys() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK17QtVirtualKeyboard8Settings19visibleFunctionKeysEv(
    const QtVirtualKeyboard::Settings *self) {
  return static_cast<unsigned int>(self->visibleFunctionKeys().toInt());
}

//  void
//      QtVirtualKeyboard::Settings::setVisibleFunctionKeys(QtVirtualKeyboard::KeyboardFunctionKeys
//      newVisibleFunctionKeys)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings22setVisibleFunctionKeysE6QFlagsINS_19KeyboardFunctionKeyEE(
    QtVirtualKeyboard::Settings *self,
    unsigned int newVisibleFunctionKeys) {
  self->setVisibleFunctionKeys(QtVirtualKeyboard::KeyboardFunctionKeys::fromInt(newVisibleFunctionKeys));
}

//  void QtVirtualKeyboard::Settings::resetVisibleFunctionKeys()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings24resetVisibleFunctionKeysEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetVisibleFunctionKeys();
}

//  bool QtVirtualKeyboard::Settings::closeOnReturn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings13closeOnReturnEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->closeOnReturn();
}

//  void QtVirtualKeyboard::Settings::setCloseOnReturn(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings16setCloseOnReturnEb(
    QtVirtualKeyboard::Settings *self,
    bool enable) {
  self->setCloseOnReturn(enable);
}

//  void QtVirtualKeyboard::Settings::resetCloseOnReturn()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings18resetCloseOnReturnEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetCloseOnReturn();
}

//  qreal QtVirtualKeyboard::Settings::keySoundVolume() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QtVirtualKeyboard8Settings14keySoundVolumeEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->keySoundVolume();
}

//  void QtVirtualKeyboard::Settings::setKeySoundVolume(qreal volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings17setKeySoundVolumeEd(
    QtVirtualKeyboard::Settings *self,
    double volume) {
  self->setKeySoundVolume(volume);
}

//  void QtVirtualKeyboard::Settings::resetKeySoundVolume()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19resetKeySoundVolumeEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetKeySoundVolume();
}

//  bool QtVirtualKeyboard::Settings::arrowKeyNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard8Settings25arrowKeyNavigationEnabledEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->arrowKeyNavigationEnabled();
}

//  void QtVirtualKeyboard::Settings::setArrowKeyNavigationEnabled(bool
//      arrowKeyNavigationEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings28setArrowKeyNavigationEnabledEb(
    QtVirtualKeyboard::Settings *self,
    bool arrowKeyNavigationEnabled) {
  self->setArrowKeyNavigationEnabled(arrowKeyNavigationEnabled);
}

//  void QtVirtualKeyboard::Settings::resetArrowKeyNavigationEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings30resetArrowKeyNavigationEnabledEv(
    QtVirtualKeyboard::Settings *self) {
  self->resetArrowKeyNavigationEnabled();
}

//  void QtVirtualKeyboard::Settings::styleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings12styleChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->styleChanged();
}

//  void QtVirtualKeyboard::Settings::styleNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings16styleNameChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->styleNameChanged();
}

//  void QtVirtualKeyboard::Settings::requestResetStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings17requestResetStyleEv(
    QtVirtualKeyboard::Settings *self) {
  self->requestResetStyle();
}

//  void QtVirtualKeyboard::Settings::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings13localeChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->localeChanged();
}

//  void QtVirtualKeyboard::Settings::availableLocalesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings23availableLocalesChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->availableLocalesChanged();
}

//  void QtVirtualKeyboard::Settings::activeLocalesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings20activeLocalesChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->activeLocalesChanged();
}

//  void QtVirtualKeyboard::Settings::layoutPathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings17layoutPathChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->layoutPathChanged();
}

//  void QtVirtualKeyboard::Settings::wclAutoHideDelayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings23wclAutoHideDelayChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->wclAutoHideDelayChanged();
}

//  void QtVirtualKeyboard::Settings::wclAlwaysVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings23wclAlwaysVisibleChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->wclAlwaysVisibleChanged();
}

//  void QtVirtualKeyboard::Settings::wclAutoCommitWordChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings24wclAutoCommitWordChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->wclAutoCommitWordChanged();
}

//  void QtVirtualKeyboard::Settings::fullScreenModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21fullScreenModeChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->fullScreenModeChanged();
}

//  void QtVirtualKeyboard::Settings::userDataPathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings19userDataPathChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->userDataPathChanged();
}

//  void QtVirtualKeyboard::Settings::userDataReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings13userDataResetEv(
    QtVirtualKeyboard::Settings *self) {
  self->userDataReset();
}

//  void QtVirtualKeyboard::Settings::hwrTimeoutForAlphabeticChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings30hwrTimeoutForAlphabeticChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->hwrTimeoutForAlphabeticChanged();
}

//  void QtVirtualKeyboard::Settings::hwrTimeoutForCjkChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings23hwrTimeoutForCjkChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->hwrTimeoutForCjkChanged();
}

//  void QtVirtualKeyboard::Settings::inputMethodHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings23inputMethodHintsChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->inputMethodHintsChanged();
}

//  void QtVirtualKeyboard::Settings::handwritingModeDisabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings30handwritingModeDisabledChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->handwritingModeDisabledChanged();
}

//  void QtVirtualKeyboard::Settings::defaultInputMethodDisabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings33defaultInputMethodDisabledChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->defaultInputMethodDisabledChanged();
}

//  void QtVirtualKeyboard::Settings::defaultDictionaryDisabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings32defaultDictionaryDisabledChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->defaultDictionaryDisabledChanged();
}

//  void QtVirtualKeyboard::Settings::visibleFunctionKeysChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings26visibleFunctionKeysChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->visibleFunctionKeysChanged();
}

//  void QtVirtualKeyboard::Settings::closeOnReturnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings20closeOnReturnChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->closeOnReturnChanged();
}

//  void QtVirtualKeyboard::Settings::keySoundVolumeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings21keySoundVolumeChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->keySoundVolumeChanged();
}

//  void QtVirtualKeyboard::Settings::arrowKeyNavigationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard8Settings32arrowKeyNavigationEnabledChangedEv(
    QtVirtualKeyboard::Settings *self) {
  self->arrowKeyNavigationEnabledChanged();
}

//  QtVirtualKeyboard::SettingsPrivate *QtVirtualKeyboard::Settings::d_func()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::SettingsPrivate *ritual_ZN17QtVirtualKeyboard8Settings6d_funcEv(
    QtVirtualKeyboard::Settings *self) {
  return self->d_func();
}

//  const QtVirtualKeyboard::SettingsPrivate
//      *QtVirtualKeyboard::Settings::d_func() const
extern "C" Q_DECL_EXPORT
const QtVirtualKeyboard::SettingsPrivate *ritual_ZNK17QtVirtualKeyboard8Settings6d_funcEv(
    const QtVirtualKeyboard::Settings *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtVirtualKeyboard_Settings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_Settings(
    QtVirtualKeyboard::Settings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_Settings *>(self)->take(key, call);
}
