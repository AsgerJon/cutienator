//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstylehints.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qstylehints.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>

//  const QMetaObject *QStyleHints::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QStyleHints10metaObjectEv(
    const QStyleHints *self) {
  return self->metaObject();
}

//  QString QStyleHints::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QStyleHints2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyleHints::tr(s, c, n));
}

//  void QStyleHints::setMouseDoubleClickInterval(int
//      mouseDoubleClickInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints27setMouseDoubleClickIntervalEi(
    QStyleHints *self,
    int mouseDoubleClickInterval) {
  self->setMouseDoubleClickInterval(mouseDoubleClickInterval);
}

//  int QStyleHints::mouseDoubleClickInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24mouseDoubleClickIntervalEv(
    const QStyleHints *self) {
  return self->mouseDoubleClickInterval();
}

//  int QStyleHints::mouseDoubleClickDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24mouseDoubleClickDistanceEv(
    const QStyleHints *self) {
  return self->mouseDoubleClickDistance();
}

//  int QStyleHints::touchDoubleTapDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints22touchDoubleTapDistanceEv(
    const QStyleHints *self) {
  return self->touchDoubleTapDistance();
}

//  void QStyleHints::setMousePressAndHoldInterval(int
//      mousePressAndHoldInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints28setMousePressAndHoldIntervalEi(
    QStyleHints *self,
    int mousePressAndHoldInterval) {
  self->setMousePressAndHoldInterval(mousePressAndHoldInterval);
}

//  int QStyleHints::mousePressAndHoldInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints25mousePressAndHoldIntervalEv(
    const QStyleHints *self) {
  return self->mousePressAndHoldInterval();
}

//  void QStyleHints::setStartDragDistance(int startDragDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints20setStartDragDistanceEi(
    QStyleHints *self,
    int startDragDistance) {
  self->setStartDragDistance(startDragDistance);
}

//  int QStyleHints::startDragDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17startDragDistanceEv(const QStyleHints *self) {
  return self->startDragDistance();
}

//  void QStyleHints::setStartDragTime(int startDragTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints16setStartDragTimeEi(
    QStyleHints *self,
    int startDragTime) {
  self->setStartDragTime(startDragTime);
}

//  int QStyleHints::startDragTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints13startDragTimeEv(const QStyleHints *self) {
  return self->startDragTime();
}

//  int QStyleHints::startDragVelocity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17startDragVelocityEv(const QStyleHints *self) {
  return self->startDragVelocity();
}

//  void QStyleHints::setKeyboardInputInterval(int keyboardInputInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints24setKeyboardInputIntervalEi(
    QStyleHints *self,
    int keyboardInputInterval) {
  self->setKeyboardInputInterval(keyboardInputInterval);
}

//  int QStyleHints::keyboardInputInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints21keyboardInputIntervalEv(
    const QStyleHints *self) {
  return self->keyboardInputInterval();
}

//  int QStyleHints::keyboardAutoRepeatRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints22keyboardAutoRepeatRateEv(
    const QStyleHints *self) {
  return self->keyboardAutoRepeatRate();
}

//  qreal QStyleHints::keyboardAutoRepeatRateF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QStyleHints23keyboardAutoRepeatRateFEv(
    const QStyleHints *self) {
  return self->keyboardAutoRepeatRateF();
}

//  void QStyleHints::setCursorFlashTime(int cursorFlashTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints18setCursorFlashTimeEi(
    QStyleHints *self,
    int cursorFlashTime) {
  self->setCursorFlashTime(cursorFlashTime);
}

//  int QStyleHints::cursorFlashTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints15cursorFlashTimeEv(const QStyleHints *self) {
  return self->cursorFlashTime();
}

//  bool QStyleHints::showIsFullScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints16showIsFullScreenEv(const QStyleHints *self) {
  return self->showIsFullScreen();
}

//  bool QStyleHints::showIsMaximized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints15showIsMaximizedEv(const QStyleHints *self) {
  return self->showIsMaximized();
}

//  bool QStyleHints::showShortcutsInContextMenus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints27showShortcutsInContextMenusEv(
    const QStyleHints *self) {
  return self->showShortcutsInContextMenus();
}

//  void QStyleHints::setShowShortcutsInContextMenus(bool
//      showShortcutsInContextMenus)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints30setShowShortcutsInContextMenusEb(
    QStyleHints *self,
    bool showShortcutsInContextMenus) {
  self->setShowShortcutsInContextMenus(showShortcutsInContextMenus);
}

//  Qt::ContextMenuTrigger QStyleHints::contextMenuTrigger() const
extern "C" Q_DECL_EXPORT
Qt::ContextMenuTrigger ritual_ZNK11QStyleHints18contextMenuTriggerEv(
    const QStyleHints *self) {
  return self->contextMenuTrigger();
}

//  void QStyleHints::setContextMenuTrigger(Qt::ContextMenuTrigger
//      contextMenuTrigger)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints21setContextMenuTriggerEN2Qt18ContextMenuTriggerE(
    QStyleHints *self,
    Qt::ContextMenuTrigger contextMenuTrigger) {
  self->setContextMenuTrigger(contextMenuTrigger);
}

//  bool QStyleHints::menuSelectionWraps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints18menuSelectionWrapsEv(const QStyleHints *self) {
  return self->menuSelectionWraps();
}

//  int QStyleHints::passwordMaskDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17passwordMaskDelayEv(const QStyleHints *self) {
  return self->passwordMaskDelay();
}

//  QChar QStyleHints::passwordMaskCharacter() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStyleHints21passwordMaskCharacterEv(
    const QStyleHints *self) {
  return new QChar(self->passwordMaskCharacter());
}

//  qreal QStyleHints::fontSmoothingGamma() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QStyleHints18fontSmoothingGammaEv(
    const QStyleHints *self) {
  return self->fontSmoothingGamma();
}

//  bool QStyleHints::useRtlExtensions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints16useRtlExtensionsEv(const QStyleHints *self) {
  return self->useRtlExtensions();
}

//  bool QStyleHints::setFocusOnTouchRelease() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints22setFocusOnTouchReleaseEv(
    const QStyleHints *self) {
  return self->setFocusOnTouchRelease();
}

//  Qt::TabFocusBehavior QStyleHints::tabFocusBehavior() const
extern "C" Q_DECL_EXPORT
Qt::TabFocusBehavior ritual_ZNK11QStyleHints16tabFocusBehaviorEv(
    const QStyleHints *self) {
  return self->tabFocusBehavior();
}

//  void QStyleHints::setTabFocusBehavior(Qt::TabFocusBehavior
//      tabFocusBehavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints19setTabFocusBehaviorEN2Qt16TabFocusBehaviorE(
    QStyleHints *self,
    Qt::TabFocusBehavior tabFocusBehavior) {
  self->setTabFocusBehavior(tabFocusBehavior);
}

//  bool QStyleHints::singleClickActivation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints21singleClickActivationEv(
    const QStyleHints *self) {
  return self->singleClickActivation();
}

//  bool QStyleHints::useHoverEffects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints15useHoverEffectsEv(const QStyleHints *self) {
  return self->useHoverEffects();
}

//  void QStyleHints::setUseHoverEffects(bool useHoverEffects)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints18setUseHoverEffectsEb(
    QStyleHints *self,
    bool useHoverEffects) {
  self->setUseHoverEffects(useHoverEffects);
}

//  int QStyleHints::wheelScrollLines() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints16wheelScrollLinesEv(const QStyleHints *self) {
  return self->wheelScrollLines();
}

//  void QStyleHints::setWheelScrollLines(int scrollLines)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints19setWheelScrollLinesEi(
    QStyleHints *self,
    int scrollLines) {
  self->setWheelScrollLines(scrollLines);
}

//  void QStyleHints::setMouseQuickSelectionThreshold(int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints31setMouseQuickSelectionThresholdEi(
    QStyleHints *self,
    int threshold) {
  self->setMouseQuickSelectionThreshold(threshold);
}

//  int QStyleHints::mouseQuickSelectionThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints28mouseQuickSelectionThresholdEv(
    const QStyleHints *self) {
  return self->mouseQuickSelectionThreshold();
}

//  Qt::ColorScheme QStyleHints::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK11QStyleHints11colorSchemeEv(
    const QStyleHints *self) {
  return self->colorScheme();
}

//  void QStyleHints::setColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints14setColorSchemeEN2Qt11ColorSchemeE(
    QStyleHints *self,
    Qt::ColorScheme scheme) {
  self->setColorScheme(scheme);
}

//  void QStyleHints::unsetColorScheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints16unsetColorSchemeEv(QStyleHints *self) {
  self->unsetColorScheme();
}

//  const QAccessibilityHints *QStyleHints::accessibility() const
extern "C" Q_DECL_EXPORT
const QAccessibilityHints *ritual_ZNK11QStyleHints13accessibilityEv(
    const QStyleHints *self) {
  return self->accessibility();
}

//  int QStyleHints::toolTipWakeUpDelayAsMSec() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24toolTipWakeUpDelayAsMSecEv(
    const QStyleHints *self) {
  return self->toolTipWakeUpDelayAsMSec();
}

//  QStyleHints::QStyleHints()
extern "C" Q_DECL_EXPORT
QStyleHints *ritual_ZN11QStyleHintsC1Ev() {
  return new QStyleHints();
}
