//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengldebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopengldebug.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpenGLDebugLogger that Python can take functions over in. Every QOpenGLDebugLogger
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLDebugLoggerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLDebugLoggerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLDebugLoggerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLDebugLoggerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLDebugLoggerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLDebugLoggerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLDebugLoggerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLDebugLogger : public QOpenGLDebugLogger {
public:
  using QOpenGLDebugLogger::QOpenGLDebugLogger;
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
      CuteQOpenGLDebugLoggerCall0 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall0>(taken[0]);
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
      CuteQOpenGLDebugLoggerCall1 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall1>(taken[1]);
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
      CuteQOpenGLDebugLoggerCall2 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall2>(taken[2]);
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
      CuteQOpenGLDebugLoggerCall3 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall3>(taken[3]);
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
      CuteQOpenGLDebugLoggerCall4 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall4>(taken[4]);
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
      CuteQOpenGLDebugLoggerCall5 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall5>(taken[5]);
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
      CuteQOpenGLDebugLoggerCall6 call = reinterpret_cast<CuteQOpenGLDebugLoggerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLDebugLogger::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QOpenGLDebugLogger10metaObjectEv(
    const QOpenGLDebugLogger *self) {
  return self->metaObject();
}

//  void *QOpenGLDebugLogger::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QOpenGLDebugLogger11qt_metacastEPKc(
    QOpenGLDebugLogger *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLDebugLogger::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QOpenGLDebugLogger11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLDebugLogger *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLDebugLogger::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QOpenGLDebugLogger2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLDebugLogger::tr(s, c, n));
}

//  QOpenGLDebugLogger::QOpenGLDebugLogger(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLDebugLogger *ritual_ZN18QOpenGLDebugLoggerC1EP7QObject(
    QObject *parent) {
  return new CuteQOpenGLDebugLogger(parent);
}

//  QOpenGLDebugLogger::~QOpenGLDebugLogger()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLoggerD1Ev(QOpenGLDebugLogger *self) {
  delete self;
}

//  bool QOpenGLDebugLogger::initialize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QOpenGLDebugLogger10initializeEv(QOpenGLDebugLogger *self) {
  return self->initialize();
}

//  bool QOpenGLDebugLogger::isLogging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QOpenGLDebugLogger9isLoggingEv(
    const QOpenGLDebugLogger *self) {
  return self->isLogging();
}

//  LoggingMode QOpenGLDebugLogger::loggingMode() const
extern "C" Q_DECL_EXPORT
QOpenGLDebugLogger::LoggingMode ritual_ZNK18QOpenGLDebugLogger11loggingModeEv(
    const QOpenGLDebugLogger *self) {
  return self->loggingMode();
}

//  qint64 QOpenGLDebugLogger::maximumMessageLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QOpenGLDebugLogger20maximumMessageLengthEv(
    const QOpenGLDebugLogger *self) {
  return self->maximumMessageLength();
}

//  void QOpenGLDebugLogger::pushGroup(const QString &name, GLuint id,
//      QOpenGLDebugMessage::Source source)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger9pushGroupERK7QStringjN19QOpenGLDebugMessage6SourceE(
    QOpenGLDebugLogger *self,
    const QString *name,
    GLuint id,
    QOpenGLDebugMessage::Source source) {
  self->pushGroup(*name, id, source);
}

//  void QOpenGLDebugLogger::popGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger8popGroupEv(QOpenGLDebugLogger *self) {
  self->popGroup();
}

//  void QOpenGLDebugLogger::enableMessages(QOpenGLDebugMessage::Sources
//      sources, QOpenGLDebugMessage::Types types,
//      QOpenGLDebugMessage::Severities severities)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger14enableMessagesE6QFlagsIN19QOpenGLDebugMessage6SourceEES0_INS1_4TypeEES0_INS1_8SeverityEE(
    QOpenGLDebugLogger *self,
    int sources,
    int types,
    int severities) {
  self->enableMessages(
      QFlags<QOpenGLDebugMessage::Source>::fromInt(sources),
      QFlags<QOpenGLDebugMessage::Type>::fromInt(types),
      QFlags<QOpenGLDebugMessage::Severity>::fromInt(severities));
}

//  void QOpenGLDebugLogger::enableMessages(const QList<GLuint> &ids,
//      QOpenGLDebugMessage::Sources sources, QOpenGLDebugMessage::Types
//      types)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger14enableMessagesERK5QListIjE6QFlagsIN19QOpenGLDebugMessage6SourceEES4_INS5_4TypeEE(
    QOpenGLDebugLogger *self,
    const QList<GLuint> *ids,
    int sources,
    int types) {
  self->enableMessages(
      *ids,
      QFlags<QOpenGLDebugMessage::Source>::fromInt(sources),
      QFlags<QOpenGLDebugMessage::Type>::fromInt(types));
}

//  void QOpenGLDebugLogger::disableMessages(QOpenGLDebugMessage::Sources
//      sources, QOpenGLDebugMessage::Types types,
//      QOpenGLDebugMessage::Severities severities)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger15disableMessagesE6QFlagsIN19QOpenGLDebugMessage6SourceEES0_INS1_4TypeEES0_INS1_8SeverityEE(
    QOpenGLDebugLogger *self,
    int sources,
    int types,
    int severities) {
  self->disableMessages(
      QFlags<QOpenGLDebugMessage::Source>::fromInt(sources),
      QFlags<QOpenGLDebugMessage::Type>::fromInt(types),
      QFlags<QOpenGLDebugMessage::Severity>::fromInt(severities));
}

//  void QOpenGLDebugLogger::disableMessages(const QList<GLuint> &ids,
//      QOpenGLDebugMessage::Sources sources, QOpenGLDebugMessage::Types
//      types)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger15disableMessagesERK5QListIjE6QFlagsIN19QOpenGLDebugMessage6SourceEES4_INS5_4TypeEE(
    QOpenGLDebugLogger *self,
    const QList<GLuint> *ids,
    int sources,
    int types) {
  self->disableMessages(
      *ids,
      QFlags<QOpenGLDebugMessage::Source>::fromInt(sources),
      QFlags<QOpenGLDebugMessage::Type>::fromInt(types));
}

//  QList<QOpenGLDebugMessage> QOpenGLDebugLogger::loggedMessages() const
extern "C" Q_DECL_EXPORT
QList<QOpenGLDebugMessage> *ritual_ZNK18QOpenGLDebugLogger14loggedMessagesEv(
    const QOpenGLDebugLogger *self) {
  return new QList<QOpenGLDebugMessage>(self->loggedMessages());
}

//  void QOpenGLDebugLogger::logMessage(const QOpenGLDebugMessage
//      &debugMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger10logMessageERK19QOpenGLDebugMessage(
    QOpenGLDebugLogger *self,
    const QOpenGLDebugMessage *debugMessage) {
  self->logMessage(*debugMessage);
}

//  void QOpenGLDebugLogger::startLogging(LoggingMode loggingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger12startLoggingENS_11LoggingModeE(
    QOpenGLDebugLogger *self,
    QOpenGLDebugLogger::LoggingMode loggingMode) {
  self->startLogging(loggingMode);
}

//  void QOpenGLDebugLogger::stopLogging()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger11stopLoggingEv(QOpenGLDebugLogger *self) {
  self->stopLogging();
}

//  void QOpenGLDebugLogger::messageLogged(const QOpenGLDebugMessage
//      &debugMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLDebugLogger13messageLoggedERK19QOpenGLDebugMessage(
    QOpenGLDebugLogger *self,
    const QOpenGLDebugMessage *debugMessage) {
  self->messageLogged(*debugMessage);
}

//  QOpenGLDebugLoggerPrivate *QOpenGLDebugLogger::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLDebugLoggerPrivate *ritual_ZN18QOpenGLDebugLogger6d_funcEv(
    QOpenGLDebugLogger *self) {
  return self->d_func();
}

//  const QOpenGLDebugLoggerPrivate *QOpenGLDebugLogger::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLDebugLoggerPrivate *ritual_ZNK18QOpenGLDebugLogger6d_funcEv(
    const QOpenGLDebugLogger *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOpenGLDebugLogger, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLDebugLogger(
    QOpenGLDebugLogger *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLDebugLogger *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_OPENGL)
