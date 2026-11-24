//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
#include <QtCore/qprocess.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QProcess that Python can take functions over in. Every QProcess
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef bool (*CuteQProcessCall0)(const void *, int, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef bool (*CuteQProcessCall1)(const void *, int, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef bool (*CuteQProcessCall2)(const void *, int, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef qint64 (*CuteQProcessCall3)(const void *, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef bool (*CuteQProcessCall4)(const void *, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
typedef void (*CuteQProcessCall5)(const void *, int *);
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
typedef qint64 (*CuteQProcessCall6)(const void *, int *);
typedef qint64 (*CuteQProcessCall7)(const void *, int *);
typedef bool (*CuteQProcessCall8)(const void *, qint64, int *);
typedef bool (*CuteQProcessCall9)(const void *, int *);
typedef bool (*CuteQProcessCall10)(const void *, int *);
typedef qint64 (*CuteQProcessCall11)(const void *, int *);
typedef bool (*CuteQProcessCall12)(const void *, int *);
typedef qint64 (*CuteQProcessCall13)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQProcessCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQProcessCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProcessCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProcessCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProcessCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProcessCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProcessCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQProcess : public QProcess {
public:
  using QProcess::QProcess;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  bool QProcess::open(OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQProcessCall0 call = reinterpret_cast<CuteQProcessCall0>(taken[0]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QProcess::open(mode);
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  bool QProcess::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProcessCall1 call = reinterpret_cast<CuteQProcessCall1>(taken[1]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QProcess::waitForReadyRead(msecs);
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  bool QProcess::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[2]) {
      int handled = 0;
      CuteQProcessCall2 call = reinterpret_cast<CuteQProcessCall2>(taken[2]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QProcess::waitForBytesWritten(msecs);
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  qint64 QProcess::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQProcessCall3 call = reinterpret_cast<CuteQProcessCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QProcess::bytesToWrite();
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  bool QProcess::isSequential() const
  bool isSequential() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQProcessCall4 call = reinterpret_cast<CuteQProcessCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QProcess::isSequential();
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
  //  void QProcess::close()
  void close() override {
    if (taken[5]) {
      int handled = 0;
      CuteQProcessCall5 call = reinterpret_cast<CuteQProcessCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QProcess::close();
  }
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQProcessCall6 call = reinterpret_cast<CuteQProcessCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQProcessCall7 call = reinterpret_cast<CuteQProcessCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[8]) {
      int handled = 0;
      CuteQProcessCall8 call = reinterpret_cast<CuteQProcessCall8>(taken[8]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQProcessCall9 call = reinterpret_cast<CuteQProcessCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[10]) {
      int handled = 0;
      CuteQProcessCall10 call = reinterpret_cast<CuteQProcessCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQProcessCall11 call = reinterpret_cast<CuteQProcessCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQProcessCall12 call = reinterpret_cast<CuteQProcessCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQProcessCall13 call = reinterpret_cast<CuteQProcessCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQProcessCall14 call = reinterpret_cast<CuteQProcessCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQProcessCall15 call = reinterpret_cast<CuteQProcessCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQProcessCall16 call = reinterpret_cast<CuteQProcessCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQProcessCall17 call = reinterpret_cast<CuteQProcessCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQProcessCall18 call = reinterpret_cast<CuteQProcessCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQProcessCall19 call = reinterpret_cast<CuteQProcessCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQProcessCall20 call = reinterpret_cast<CuteQProcessCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

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
  return new CuteQProcess(parent);
}

//  QProcess::~QProcess()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcessD1Ev(QProcess *self) {
  delete self;
}

//  void QProcess::start(const QString &program, const QStringList
//      &arguments, OpenMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess5startERK7QStringRK5QListIS0_E6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    const QString *program,
    const QList<QString> *arguments,
    int mode) {
  self->start(
      *program,
      *arguments,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
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

//  QStringList QProcess::arguments() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QProcess9argumentsEv(const QProcess *self) {
  return new QList<QString>(self->arguments());
}

//  void QProcess::setArguments(const QStringList &arguments)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess12setArgumentsERK5QListI7QStringE(
    QProcess *self,
    const QList<QString> *arguments) {
  self->setArguments(*arguments);
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

#if defined(Q_OS_UNIX) || defined(Q_QDOC)
//  void QProcess::failChildProcessModifier(const char *description, int
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24failChildProcessModifierEPKci(
    QProcess *self,
    const char *description,
    int error) {
  self->failChildProcessModifier(description, error);
}
#endif  // defined(Q_OS_UNIX) || defined(Q_QDOC)

#if defined(Q_OS_UNIX) || defined(Q_QDOC)
//  UnixProcessParameters QProcess::unixProcessParameters() const
extern "C" Q_DECL_EXPORT
QProcess::UnixProcessParameters *ritual_ZNK8QProcess21unixProcessParametersEv(
    const QProcess *self) {
  return new QProcess::UnixProcessParameters(self->unixProcessParameters());
}
#endif  // defined(Q_OS_UNIX) || defined(Q_QDOC)

#if defined(Q_OS_UNIX) || defined(Q_QDOC)
//  void QProcess::setUnixProcessParameters(const UnixProcessParameters
//      &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24setUnixProcessParametersERKNS_21UnixProcessParametersE(
    QProcess *self,
    const QProcess::UnixProcessParameters *params) {
  self->setUnixProcessParameters(*params);
}
#endif  // defined(Q_OS_UNIX) || defined(Q_QDOC)

#if defined(Q_OS_UNIX) || defined(Q_QDOC)
//  void QProcess::setUnixProcessParameters(UnixProcessFlags flagsOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess24setUnixProcessParametersE6QFlagsINS_15UnixProcessFlagEE(
    QProcess *self,
    int flagsOnly) {
  self->setUnixProcessParameters(
      QFlags<QProcess::UnixProcessFlag>::fromInt(flagsOnly));
}
#endif  // defined(Q_OS_UNIX) || defined(Q_QDOC)

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

//  void QProcess::setEnvironment(const QStringList &environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess14setEnvironmentERK5QListI7QStringE(
    QProcess *self,
    const QList<QString> *environment) {
  self->setEnvironment(*environment);
}

//  QStringList QProcess::environment() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QProcess11environmentEv(const QProcess *self) {
  return new QList<QString>(self->environment());
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

//  int QProcess::execute(const QString &program, const QStringList
//      &arguments)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QProcess7executeERK7QStringRK5QListIS0_E(
    const QString *program,
    const QList<QString> *arguments) {
  return QProcess::execute(*program, *arguments);
}

//  bool QProcess::startDetached(const QString &program, const QStringList
//      &arguments, const QString &workingDirectory, qint64 *pid)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QProcess13startDetachedERK7QStringRK5QListIS0_ES2_Px(
    const QString *program,
    const QList<QString> *arguments,
    const QString *workingDirectory,
    qint64 *pid) {
  return QProcess::startDetached(
      *program,
      *arguments,
      *workingDirectory,
      pid);
}

//  QStringList QProcess::systemEnvironment()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN8QProcess17systemEnvironmentEv() {
  return new QList<QString>(QProcess::systemEnvironment());
}

//  QString QProcess::nullDevice()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QProcess10nullDeviceEv() {
  return new QString(QProcess::nullDevice());
}

//  QStringList QProcess::splitCommand(QStringView command)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN8QProcess12splitCommandE11QStringView(
    const QString *command) {
  return new QList<QString>(QProcess::splitCommand(QStringView(*command)));
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

//  void QProcess::setProcessState(ProcessState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess15setProcessStateENS_12ProcessStateE(
    QProcess *self,
    QProcess::ProcessState state) {
  self->setProcessState(state);
}

//  qint64 QProcess::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN8QProcess9writeDataEPKcx(
    QProcess *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  QProcessPrivate *QProcess::d_func()
extern "C" Q_DECL_EXPORT
QProcessPrivate *ritual_ZN8QProcess6d_funcEv(QProcess *self) {
  return self->d_func();
}

//  const QProcessPrivate *QProcess::d_func() const
extern "C" Q_DECL_EXPORT
const QProcessPrivate *ritual_ZNK8QProcess6d_funcEv(const QProcess *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQProcess, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProcess(QProcess *self, const char *key, void *call) {
  return static_cast<CuteQProcess *>(self)->take(key, call);
}

//  bool QProcess::open(OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QProcess4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QProcess *self,
    int mode) {
  return self->QProcess::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  bool QProcess::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QProcess16waitForReadyReadEi(QProcess *self, int msecs) {
  return self->QProcess::waitForReadyRead(msecs);
}

//  bool QProcess::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QProcess19waitForBytesWrittenEi(
    QProcess *self,
    int msecs) {
  return self->QProcess::waitForBytesWritten(msecs);
}

//  qint64 QProcess::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK8QProcess12bytesToWriteEv(const QProcess *self) {
  return self->QProcess::bytesToWrite();
}

//  bool QProcess::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QProcess12isSequentialEv(const QProcess *self) {
  return self->QProcess::isSequential();
}

//  void QProcess::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QProcess5closeEv(QProcess *self) {
  self->QProcess::close();
}

#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
