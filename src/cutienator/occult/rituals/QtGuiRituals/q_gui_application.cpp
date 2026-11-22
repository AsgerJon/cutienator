//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qguiapplication.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qguiapplication.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qicon.h>
#include <QtGui/qcursor.h>
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>

//  const QMetaObject *QGuiApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGuiApplication10metaObjectEv(
    const QGuiApplication *self) {
  return self->metaObject();
}

//  QString QGuiApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGuiApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGuiApplication::tr(s, c, n));
}

//  QGuiApplication::QGuiApplication(int &argc, char **argv, int a2)
extern "C" Q_DECL_EXPORT
QGuiApplication *ritual_ZN15QGuiApplicationC1ERiPPci(
    int *argc,
    char **argv,
    int a2) {
  return new QGuiApplication(*argc, argv, a2);
}

//  QGuiApplication::~QGuiApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplicationD1Ev(QGuiApplication *self) {
  delete self;
}

//  void QGuiApplication::setApplicationDisplayName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication25setApplicationDisplayNameERK7QString(
    const QString *name) {
  QGuiApplication::setApplicationDisplayName(*name);
}

//  QString QGuiApplication::applicationDisplayName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGuiApplication22applicationDisplayNameEv() {
  return new QString(QGuiApplication::applicationDisplayName());
}

//  void QGuiApplication::setBadgeNumber(qint64 number)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication14setBadgeNumberEx(
    QGuiApplication *self,
    qint64 number) {
  self->setBadgeNumber(number);
}

//  void QGuiApplication::setDesktopFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication18setDesktopFileNameERK7QString(
    const QString *name) {
  QGuiApplication::setDesktopFileName(*name);
}

//  QString QGuiApplication::desktopFileName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGuiApplication15desktopFileNameEv() {
  return new QString(QGuiApplication::desktopFileName());
}

//  QWindow *QGuiApplication::topLevelAt(const QPoint &pos)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN15QGuiApplication10topLevelAtERK6QPoint(
    const QPoint *pos) {
  return QGuiApplication::topLevelAt(*pos);
}

//  void QGuiApplication::setWindowIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication13setWindowIconERK5QIcon(const QIcon *icon) {
  QGuiApplication::setWindowIcon(*icon);
}

//  QIcon QGuiApplication::windowIcon()
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN15QGuiApplication10windowIconEv() {
  return new QIcon(QGuiApplication::windowIcon());
}

//  QString QGuiApplication::platformName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGuiApplication12platformNameEv() {
  return new QString(QGuiApplication::platformName());
}

//  QWindow *QGuiApplication::modalWindow()
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN15QGuiApplication11modalWindowEv() {
  return QGuiApplication::modalWindow();
}

//  QWindow *QGuiApplication::focusWindow()
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN15QGuiApplication11focusWindowEv() {
  return QGuiApplication::focusWindow();
}

//  QObject *QGuiApplication::focusObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN15QGuiApplication11focusObjectEv() {
  return QGuiApplication::focusObject();
}

//  QScreen *QGuiApplication::primaryScreen()
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN15QGuiApplication13primaryScreenEv() {
  return QGuiApplication::primaryScreen();
}

//  QScreen *QGuiApplication::screenAt(const QPoint &point)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN15QGuiApplication8screenAtERK6QPoint(const QPoint *point) {
  return QGuiApplication::screenAt(*point);
}

//  qreal QGuiApplication::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QGuiApplication16devicePixelRatioEv(
    const QGuiApplication *self) {
  return self->devicePixelRatio();
}

//  QCursor *QGuiApplication::overrideCursor()
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN15QGuiApplication14overrideCursorEv() {
  return QGuiApplication::overrideCursor();
}

//  void QGuiApplication::setOverrideCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication17setOverrideCursorERK7QCursor(
    const QCursor *a0) {
  QGuiApplication::setOverrideCursor(*a0);
}

//  void QGuiApplication::changeOverrideCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication20changeOverrideCursorERK7QCursor(
    const QCursor *a0) {
  QGuiApplication::changeOverrideCursor(*a0);
}

//  void QGuiApplication::restoreOverrideCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication21restoreOverrideCursorEv() {
  QGuiApplication::restoreOverrideCursor();
}

//  QFont QGuiApplication::font()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN15QGuiApplication4fontEv() {
  return new QFont(QGuiApplication::font());
}

//  void QGuiApplication::setFont(const QFont &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication7setFontERK5QFont(const QFont *a0) {
  QGuiApplication::setFont(*a0);
}

//  QClipboard *QGuiApplication::clipboard()
extern "C" Q_DECL_EXPORT
QClipboard *ritual_ZN15QGuiApplication9clipboardEv() {
  return QGuiApplication::clipboard();
}

//  QPalette QGuiApplication::palette()
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN15QGuiApplication7paletteEv() {
  return new QPalette(QGuiApplication::palette());
}

//  void QGuiApplication::setPalette(const QPalette &pal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication10setPaletteERK8QPalette(
    const QPalette *pal) {
  QGuiApplication::setPalette(*pal);
}

//  Qt::KeyboardModifiers QGuiApplication::keyboardModifiers()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGuiApplication17keyboardModifiersEv() {
  return static_cast<int>(QGuiApplication::keyboardModifiers().toInt());
}

//  Qt::KeyboardModifiers QGuiApplication::queryKeyboardModifiers()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGuiApplication22queryKeyboardModifiersEv() {
  return static_cast<int>(QGuiApplication::queryKeyboardModifiers().toInt());
}

//  Qt::MouseButtons QGuiApplication::mouseButtons()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGuiApplication12mouseButtonsEv() {
  return static_cast<int>(QGuiApplication::mouseButtons().toInt());
}

//  void QGuiApplication::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication18setLayoutDirectionEN2Qt15LayoutDirectionE(
    Qt::LayoutDirection direction) {
  QGuiApplication::setLayoutDirection(direction);
}

//  Qt::LayoutDirection QGuiApplication::layoutDirection()
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZN15QGuiApplication15layoutDirectionEv() {
  return QGuiApplication::layoutDirection();
}

//  bool QGuiApplication::isRightToLeft()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGuiApplication13isRightToLeftEv() {
  return QGuiApplication::isRightToLeft();
}

//  bool QGuiApplication::isLeftToRight()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGuiApplication13isLeftToRightEv() {
  return QGuiApplication::isLeftToRight();
}

//  QStyleHints *QGuiApplication::styleHints()
extern "C" Q_DECL_EXPORT
QStyleHints *ritual_ZN15QGuiApplication10styleHintsEv() {
  return QGuiApplication::styleHints();
}

//  void QGuiApplication::setDesktopSettingsAware(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication23setDesktopSettingsAwareEb(bool on) {
  QGuiApplication::setDesktopSettingsAware(on);
}

//  bool QGuiApplication::desktopSettingsAware()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGuiApplication20desktopSettingsAwareEv() {
  return QGuiApplication::desktopSettingsAware();
}

//  QInputMethod *QGuiApplication::inputMethod()
extern "C" Q_DECL_EXPORT
QInputMethod *ritual_ZN15QGuiApplication11inputMethodEv() {
  return QGuiApplication::inputMethod();
}

//  void QGuiApplication::setQuitOnLastWindowClosed(bool quit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication25setQuitOnLastWindowClosedEb(bool quit) {
  QGuiApplication::setQuitOnLastWindowClosed(quit);
}

//  bool QGuiApplication::quitOnLastWindowClosed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGuiApplication22quitOnLastWindowClosedEv() {
  return QGuiApplication::quitOnLastWindowClosed();
}

//  Qt::ApplicationState QGuiApplication::applicationState()
extern "C" Q_DECL_EXPORT
Qt::ApplicationState ritual_ZN15QGuiApplication16applicationStateEv() {
  return QGuiApplication::applicationState();
}

//  void QGuiApplication::setHighDpiScaleFactorRoundingPolicy(Qt::HighDpiScal
//      eFactorRoundingPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication35setHighDpiScaleFactorRoundingPolicyEN2Qt32HighDpiScaleFactorRoundingPolicyE(
    Qt::HighDpiScaleFactorRoundingPolicy policy) {
  QGuiApplication::setHighDpiScaleFactorRoundingPolicy(policy);
}

//  Qt::HighDpiScaleFactorRoundingPolicy
//      QGuiApplication::highDpiScaleFactorRoundingPolicy()
extern "C" Q_DECL_EXPORT
Qt::HighDpiScaleFactorRoundingPolicy ritual_ZN15QGuiApplication32highDpiScaleFactorRoundingPolicyEv() {
  return QGuiApplication::highDpiScaleFactorRoundingPolicy();
}

//  int QGuiApplication::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGuiApplication4execEv() {
  return QGuiApplication::exec();
}

//  bool QGuiApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGuiApplication6notifyEP7QObjectP6QEvent(
    QGuiApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->notify(a0, a1);
}

//  bool QGuiApplication::isSessionRestored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGuiApplication17isSessionRestoredEv(
    const QGuiApplication *self) {
  return self->isSessionRestored();
}

//  QString QGuiApplication::sessionId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QGuiApplication9sessionIdEv(
    const QGuiApplication *self) {
  return new QString(self->sessionId());
}

//  QString QGuiApplication::sessionKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QGuiApplication10sessionKeyEv(
    const QGuiApplication *self) {
  return new QString(self->sessionKey());
}

//  bool QGuiApplication::isSavingSession() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGuiApplication15isSavingSessionEv(
    const QGuiApplication *self) {
  return self->isSavingSession();
}

//  void QGuiApplication::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGuiApplication4syncEv() {
  QGuiApplication::sync();
}
