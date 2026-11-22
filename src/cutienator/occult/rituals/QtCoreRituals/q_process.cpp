//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qprocess.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QProcess::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QProcess10metaObjectEv(const QProcess *self) {
  return self->metaObject();
}

//  QString QProcess::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QProcess2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QProcess::tr(s, c, n));
}

//  QProcess::QProcess(QObject *parent)
extern "C" Q_DECL_EXPORT
QProcess *ritual_ZN8QProcessC1EP7QObject(QObject *parent) {
  return new QProcess(parent);
}

//  QProcess::~QProcess()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcessD1Ev(QProcess *self) {
  delete self;
}

//  void QProcess::start(OpenMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess5startE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    int mode) {
  self->start(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QProcess::startCommand(const QString &command, OpenMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess12startCommandERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    const QString *command,
    int mode) {
  self->startCommand(
      *command,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  bool QProcess::startDetached(qint64 *pid)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess13startDetachedEPx(QProcess *self, qint64 *pid) {
  return self->startDetached(pid);
}

//  bool QProcess::open(OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    int mode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QString QProcess::program() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QProcess7programEv(const QProcess *self) {
  return new QString(self->program());
}

//  void QProcess::setProgram(const QString &program)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess10setProgramERK7QString(
    QProcess *self,
    const QString *program) {
  self->setProgram(*program);
}

//  ProcessChannelMode QProcess::processChannelMode() const
extern "C" Q_DECL_EXPORT
QProcess::ProcessChannelMode ritual_ZNK8QProcess18processChannelModeEv(
    const QProcess *self) {
  return self->processChannelMode();
}

//  void QProcess::setProcessChannelMode(ProcessChannelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess21setProcessChannelModeENS_18ProcessChannelModeE(
    QProcess *self,
    QProcess::ProcessChannelMode mode) {
  self->setProcessChannelMode(mode);
}

//  InputChannelMode QProcess::inputChannelMode() const
extern "C" Q_DECL_EXPORT
QProcess::InputChannelMode ritual_ZNK8QProcess16inputChannelModeEv(
    const QProcess *self) {
  return self->inputChannelMode();
}

//  void QProcess::setInputChannelMode(InputChannelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess19setInputChannelModeENS_16InputChannelModeE(
    QProcess *self,
    QProcess::InputChannelMode mode) {
  self->setInputChannelMode(mode);
}

//  ProcessChannel QProcess::readChannel() const
extern "C" Q_DECL_EXPORT
QProcess::ProcessChannel ritual_ZNK8QProcess11readChannelEv(
    const QProcess *self) {
  return self->readChannel();
}

//  void QProcess::setReadChannel(ProcessChannel channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess14setReadChannelENS_14ProcessChannelE(
    QProcess *self,
    QProcess::ProcessChannel channel) {
  self->setReadChannel(channel);
}

//  void QProcess::closeReadChannel(ProcessChannel channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess16closeReadChannelENS_14ProcessChannelE(
    QProcess *self,
    QProcess::ProcessChannel channel) {
  self->closeReadChannel(channel);
}

//  void QProcess::closeWriteChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess17closeWriteChannelEv(QProcess *self) {
  self->closeWriteChannel();
}

//  void QProcess::setStandardInputFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess20setStandardInputFileERK7QString(
    QProcess *self,
    const QString *fileName) {
  self->setStandardInputFile(*fileName);
}

//  void QProcess::setStandardOutputFile(const QString &fileName, OpenMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess21setStandardOutputFileERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    const QString *fileName,
    int mode) {
  self->setStandardOutputFile(
      *fileName,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QProcess::setStandardErrorFile(const QString &fileName, OpenMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess20setStandardErrorFileERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    const QString *fileName,
    int mode) {
  self->setStandardErrorFile(
      *fileName,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QProcess::setStandardOutputProcess(QProcess *destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24setStandardOutputProcessEPS_(
    QProcess *self,
    QProcess *destination) {
  self->setStandardOutputProcess(destination);
}

//  void QProcess::failChildProcessModifier(const char *description, int
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24failChildProcessModifierEPKci(
    QProcess *self,
    const char *description,
    int error) {
  self->failChildProcessModifier(description, error);
}

//  UnixProcessParameters QProcess::unixProcessParameters() const
extern "C" Q_DECL_EXPORT
QProcess::UnixProcessParameters *ritual_ZNK8QProcess21unixProcessParametersEv(
    const QProcess *self) {
  return new QProcess::UnixProcessParameters(self->unixProcessParameters());
}

//  void QProcess::setUnixProcessParameters(const UnixProcessParameters
//      &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24setUnixProcessParametersERKNS_21UnixProcessParametersE(
    QProcess *self,
    const QProcess::UnixProcessParameters *params) {
  self->setUnixProcessParameters(*params);
}

//  void QProcess::setUnixProcessParameters(UnixProcessFlags flagsOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24setUnixProcessParametersE6QFlagsINS_15UnixProcessFlagEE(
    QProcess *self,
    int flagsOnly) {
  self->setUnixProcessParameters(
      QFlags<QProcess::UnixProcessFlag>::fromInt(flagsOnly));
}

//  QString QProcess::workingDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QProcess16workingDirectoryEv(const QProcess *self) {
  return new QString(self->workingDirectory());
}

//  void QProcess::setWorkingDirectory(const QString &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess19setWorkingDirectoryERK7QString(
    QProcess *self,
    const QString *dir) {
  self->setWorkingDirectory(*dir);
}

//  void QProcess::setProcessEnvironment(const QProcessEnvironment
//      &environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess21setProcessEnvironmentERK19QProcessEnvironment(
    QProcess *self,
    const QProcessEnvironment *environment) {
  self->setProcessEnvironment(*environment);
}

//  QProcessEnvironment QProcess::processEnvironment() const
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZNK8QProcess18processEnvironmentEv(
    const QProcess *self) {
  return new QProcessEnvironment(self->processEnvironment());
}

//  QProcess::ProcessError QProcess::error() const
extern "C" Q_DECL_EXPORT
QProcess::ProcessError ritual_ZNK8QProcess5errorEv(const QProcess *self) {
  return self->error();
}

//  QProcess::ProcessState QProcess::state() const
extern "C" Q_DECL_EXPORT
QProcess::ProcessState ritual_ZNK8QProcess5stateEv(const QProcess *self) {
  return self->state();
}

//  qint64 QProcess::processId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK8QProcess9processIdEv(const QProcess *self) {
  return self->processId();
}

//  bool QProcess::waitForStarted(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess14waitForStartedEi(QProcess *self, int msecs) {
  return self->waitForStarted(msecs);
}

//  bool QProcess::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess16waitForReadyReadEi(QProcess *self, int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QProcess::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess19waitForBytesWrittenEi(QProcess *self, int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QProcess::waitForFinished(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess15waitForFinishedEi(QProcess *self, int msecs) {
  return self->waitForFinished(msecs);
}

//  QByteArray QProcess::readAllStandardOutput()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QProcess21readAllStandardOutputEv(QProcess *self) {
  return new QByteArray(self->readAllStandardOutput());
}

//  QByteArray QProcess::readAllStandardError()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QProcess20readAllStandardErrorEv(QProcess *self) {
  return new QByteArray(self->readAllStandardError());
}

//  int QProcess::exitCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QProcess8exitCodeEv(const QProcess *self) {
  return self->exitCode();
}

//  QProcess::ExitStatus QProcess::exitStatus() const
extern "C" Q_DECL_EXPORT
QProcess::ExitStatus ritual_ZNK8QProcess10exitStatusEv(
    const QProcess *self) {
  return self->exitStatus();
}

//  qint64 QProcess::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK8QProcess12bytesToWriteEv(const QProcess *self) {
  return self->bytesToWrite();
}

//  bool QProcess::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QProcess12isSequentialEv(const QProcess *self) {
  return self->isSequential();
}

//  void QProcess::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess5closeEv(QProcess *self) {
  self->close();
}

//  QString QProcess::nullDevice()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QProcess10nullDeviceEv() {
  return new QString(QProcess::nullDevice());
}

//  void QProcess::terminate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess9terminateEv(QProcess *self) {
  self->terminate();
}

//  void QProcess::kill()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess4killEv(QProcess *self) {
  self->kill();
}
