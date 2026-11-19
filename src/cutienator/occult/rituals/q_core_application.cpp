//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreapplication.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreapplication.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qpermissions.h>

//  const QMetaObject *QCoreApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QCoreApplication10metaObjectEv(
    const QCoreApplication *self) {
  return self->metaObject();
}

//  QString QCoreApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoreApplication::tr(s, c, n));
}

//  QCoreApplication::QCoreApplication(int &argc, char **argv, int a2)
extern "C" Q_DECL_EXPORT
QCoreApplication *ritual_ZN16QCoreApplicationC1ERiPPci(
    int *argc,
    char **argv,
    int a2) {
  return new QCoreApplication(*argc, argv, a2);
}

//  QCoreApplication::~QCoreApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplicationD1Ev(QCoreApplication *self) {
  delete self;
}

//  void QCoreApplication::setAttribute(Qt::ApplicationAttribute attribute,
//      bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication12setAttributeEN2Qt20ApplicationAttributeEb(
    Qt::ApplicationAttribute attribute,
    bool on) {
  QCoreApplication::setAttribute(attribute, on);
}

//  bool QCoreApplication::testAttribute(Qt::ApplicationAttribute attribute)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication13testAttributeEN2Qt20ApplicationAttributeE(
    Qt::ApplicationAttribute attribute) {
  return QCoreApplication::testAttribute(attribute);
}

//  void QCoreApplication::setOrganizationDomain(const QString &orgDomain)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication21setOrganizationDomainERK7QString(
    const QString *orgDomain) {
  QCoreApplication::setOrganizationDomain(*orgDomain);
}

//  QString QCoreApplication::organizationDomain()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18organizationDomainEv() {
  return new QString(QCoreApplication::organizationDomain());
}

//  void QCoreApplication::setOrganizationName(const QString &orgName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication19setOrganizationNameERK7QString(
    const QString *orgName) {
  QCoreApplication::setOrganizationName(*orgName);
}

//  QString QCoreApplication::organizationName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication16organizationNameEv() {
  return new QString(QCoreApplication::organizationName());
}

//  void QCoreApplication::setApplicationName(const QString &application)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setApplicationNameERK7QString(
    const QString *application) {
  QCoreApplication::setApplicationName(*application);
}

//  QString QCoreApplication::applicationName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication15applicationNameEv() {
  return new QString(QCoreApplication::applicationName());
}

//  void QCoreApplication::setApplicationVersion(const QString &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication21setApplicationVersionERK7QString(
    const QString *version) {
  QCoreApplication::setApplicationVersion(*version);
}

//  QString QCoreApplication::applicationVersion()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18applicationVersionEv() {
  return new QString(QCoreApplication::applicationVersion());
}

//  void QCoreApplication::setSetuidAllowed(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication16setSetuidAllowedEb(bool allow) {
  QCoreApplication::setSetuidAllowed(allow);
}

//  bool QCoreApplication::isSetuidAllowed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication15isSetuidAllowedEv() {
  return QCoreApplication::isSetuidAllowed();
}

//  QCoreApplication *QCoreApplication::instance()
extern "C" Q_DECL_EXPORT
QCoreApplication *ritual_ZN16QCoreApplication8instanceEv() {
  return QCoreApplication::instance();
}

//  bool QCoreApplication::instanceExists()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication14instanceExistsEv() {
  return QCoreApplication::instanceExists();
}

//  int QCoreApplication::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QCoreApplication4execEv() {
  return QCoreApplication::exec();
}

//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int flags) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags, int maxtime)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEEi(
    int flags,
    int maxtime) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      maxtime);
}

//  void QCoreApplication::processEvents(QEventLoop::ProcessEventsFlags
//      flags, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer(
    int flags,
    const QDeadlineTimer *deadline) {
  QCoreApplication::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}

//  bool QCoreApplication::sendEvent(QObject *receiver, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication9sendEventEP7QObjectP6QEvent(
    QObject *receiver,
    QEvent *event) {
  return QCoreApplication::sendEvent(receiver, event);
}

//  void QCoreApplication::postEvent(QObject *receiver, QEvent *event, int
//      priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication9postEventEP7QObjectP6QEventi(
    QObject *receiver,
    QEvent *event,
    int priority) {
  QCoreApplication::postEvent(receiver, event, priority);
}

//  void QCoreApplication::sendPostedEvents(QObject *receiver, int
//      event_type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication16sendPostedEventsEP7QObjecti(
    QObject *receiver,
    int event_type) {
  QCoreApplication::sendPostedEvents(receiver, event_type);
}

//  void QCoreApplication::removePostedEvents(QObject *receiver, int
//      eventType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18removePostedEventsEP7QObjecti(
    QObject *receiver,
    int eventType) {
  QCoreApplication::removePostedEvents(receiver, eventType);
}

//  QAbstractEventDispatcher *QCoreApplication::eventDispatcher()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN16QCoreApplication15eventDispatcherEv() {
  return QCoreApplication::eventDispatcher();
}

//  void QCoreApplication::setEventDispatcher(QAbstractEventDispatcher
//      *eventDispatcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setEventDispatcherEP24QAbstractEventDispatcher(
    QAbstractEventDispatcher *eventDispatcher) {
  QCoreApplication::setEventDispatcher(eventDispatcher);
}

//  bool QCoreApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication6notifyEP7QObjectP6QEvent(
    QCoreApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->notify(a0, a1);
}

//  bool QCoreApplication::startingUp()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication10startingUpEv() {
  return QCoreApplication::startingUp();
}

//  bool QCoreApplication::closingDown()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication11closingDownEv() {
  return QCoreApplication::closingDown();
}

//  QString QCoreApplication::applicationDirPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication18applicationDirPathEv() {
  return new QString(QCoreApplication::applicationDirPath());
}

//  QString QCoreApplication::applicationFilePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication19applicationFilePathEv() {
  return new QString(QCoreApplication::applicationFilePath());
}

//  qint64 QCoreApplication::applicationPid()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QCoreApplication14applicationPidEv() {
  return QCoreApplication::applicationPid();
}

//  Qt::PermissionStatus QCoreApplication::checkPermission(const QPermission
//      &permission)
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZN16QCoreApplication15checkPermissionERK11QPermission(
    QCoreApplication *self,
    const QPermission *permission) {
  return self->checkPermission(*permission);
}

//  void QCoreApplication::addLibraryPath(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication14addLibraryPathERK7QString(
    const QString *a0) {
  QCoreApplication::addLibraryPath(*a0);
}

//  void QCoreApplication::removeLibraryPath(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication17removeLibraryPathERK7QString(
    const QString *a0) {
  QCoreApplication::removeLibraryPath(*a0);
}

//  bool QCoreApplication::installTranslator(QTranslator *messageFile)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication17installTranslatorEP11QTranslator(
    QTranslator *messageFile) {
  return QCoreApplication::installTranslator(messageFile);
}

//  bool QCoreApplication::removeTranslator(QTranslator *messageFile)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication16removeTranslatorEP11QTranslator(
    QTranslator *messageFile) {
  return QCoreApplication::removeTranslator(messageFile);
}

//  QString QCoreApplication::translate(const char *context, const char *key,
//      const char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCoreApplication9translateEPKcS1_S1_i(
    const char *context,
    const char *key,
    const char *disambiguation,
    int n) {
  return new QString(
      QCoreApplication::translate(
          context,
          key,
          disambiguation,
          n));
}

//  void
//      QCoreApplication::installNativeEventFilter(QAbstractNativeEventFilter
//      *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication24installNativeEventFilterEP26QAbstractNativeEventFilter(
    QCoreApplication *self,
    QAbstractNativeEventFilter *filterObj) {
  self->installNativeEventFilter(filterObj);
}

//  void QCoreApplication::removeNativeEventFilter(QAbstractNativeEventFilter
//      *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication23removeNativeEventFilterEP26QAbstractNativeEventFilter(
    QCoreApplication *self,
    QAbstractNativeEventFilter *filterObj) {
  self->removeNativeEventFilter(filterObj);
}

//  bool QCoreApplication::isQuitLockEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCoreApplication17isQuitLockEnabledEv() {
  return QCoreApplication::isQuitLockEnabled();
}

//  void QCoreApplication::setQuitLockEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication18setQuitLockEnabledEb(bool enabled) {
  QCoreApplication::setQuitLockEnabled(enabled);
}

//  void QCoreApplication::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication4quitEv() {
  QCoreApplication::quit();
}

//  void QCoreApplication::exit(int retcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreApplication4exitEi(int retcode) {
  QCoreApplication::exit(retcode);
}
