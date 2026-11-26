//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengldebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopengldebug.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpenGLDebugMessage::QOpenGLDebugMessage()
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessageC1Ev() {
  return new QOpenGLDebugMessage();
}

//  QOpenGLDebugMessage::QOpenGLDebugMessage(const QOpenGLDebugMessage
//      &debugMessage)
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessageC1ERKS_(
    const QOpenGLDebugMessage *debugMessage) {
  return new QOpenGLDebugMessage(*debugMessage);
}

//  QOpenGLDebugMessage &QOpenGLDebugMessage::operator=(const
//      QOpenGLDebugMessage &debugMessage)
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessageaSERKS_(
    QOpenGLDebugMessage *self,
    const QOpenGLDebugMessage *debugMessage) {
  return &(self->operator=(*debugMessage));
}

//  QOpenGLDebugMessage &QOpenGLDebugMessage::operator=(QOpenGLDebugMessage
//      &&other)
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessageaSEOS_(
    QOpenGLDebugMessage *self,
    QOpenGLDebugMessage *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpenGLDebugMessage::~QOpenGLDebugMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLDebugMessageD1Ev(QOpenGLDebugMessage *self) {
  delete self;
}

//  void QOpenGLDebugMessage::swap(QOpenGLDebugMessage &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLDebugMessage4swapERS_(
    QOpenGLDebugMessage *self,
    QOpenGLDebugMessage *other) {
  self->swap(*other);
}

//  Source QOpenGLDebugMessage::source() const
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage::Source ritual_ZNK19QOpenGLDebugMessage6sourceEv(
    const QOpenGLDebugMessage *self) {
  return self->source();
}

//  Type QOpenGLDebugMessage::type() const
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage::Type ritual_ZNK19QOpenGLDebugMessage4typeEv(
    const QOpenGLDebugMessage *self) {
  return self->type();
}

//  Severity QOpenGLDebugMessage::severity() const
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage::Severity ritual_ZNK19QOpenGLDebugMessage8severityEv(
    const QOpenGLDebugMessage *self) {
  return self->severity();
}

//  GLuint QOpenGLDebugMessage::id() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK19QOpenGLDebugMessage2idEv(
    const QOpenGLDebugMessage *self) {
  return self->id();
}

//  QString QOpenGLDebugMessage::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpenGLDebugMessage7messageEv(
    const QOpenGLDebugMessage *self) {
  return new QString(self->message());
}

//  QOpenGLDebugMessage QOpenGLDebugMessage::createApplicationMessage(const
//      QString &text, GLuint id, Severity severity, Type type)
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessage24createApplicationMessageERK7QStringjNS_8SeverityENS_4TypeE(
    const QString *text,
    GLuint id,
    QOpenGLDebugMessage::Severity severity,
    QOpenGLDebugMessage::Type type) {
  return new QOpenGLDebugMessage(
      QOpenGLDebugMessage::createApplicationMessage(
          *text,
          id,
          severity,
          type));
}

//  QOpenGLDebugMessage QOpenGLDebugMessage::createThirdPartyMessage(const
//      QString &text, GLuint id, Severity severity, Type type)
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_ZN19QOpenGLDebugMessage23createThirdPartyMessageERK7QStringjNS_8SeverityENS_4TypeE(
    const QString *text,
    GLuint id,
    QOpenGLDebugMessage::Severity severity,
    QOpenGLDebugMessage::Type type) {
  return new QOpenGLDebugMessage(
      QOpenGLDebugMessage::createThirdPartyMessage(
          *text,
          id,
          severity,
          type));
}

//  bool QOpenGLDebugMessage::operator==(const QOpenGLDebugMessage
//      &debugMessage) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpenGLDebugMessageeqERKS_(
    const QOpenGLDebugMessage *self,
    const QOpenGLDebugMessage *debugMessage) {
  return self->operator==(*debugMessage);
}

//  bool QOpenGLDebugMessage::operator!=(const QOpenGLDebugMessage
//      &debugMessage) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpenGLDebugMessageneERKS_(
    const QOpenGLDebugMessage *self,
    const QOpenGLDebugMessage *debugMessage) {
  return self->operator!=(*debugMessage);
}

//  QList<QOpenGLDebugMessage>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpenGLDebugMessage> *ritual_list_make_QOpenGLDebugMessage() {
  return new QList<QOpenGLDebugMessage>();
}

//  void QList<QOpenGLDebugMessage>::append(const QOpenGLDebugMessage &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpenGLDebugMessage(
    QList<QOpenGLDebugMessage> *self,
    const QOpenGLDebugMessage *element) {
  self->append(*element);
}

//  qsizetype QList<QOpenGLDebugMessage>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpenGLDebugMessage(
    const QList<QOpenGLDebugMessage> *self) {
  return self->size();
}

//  const QOpenGLDebugMessage &QList<QOpenGLDebugMessage>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QOpenGLDebugMessage *ritual_list_at_QOpenGLDebugMessage(
    const QList<QOpenGLDebugMessage> *self,
    long long index) {
  return new QOpenGLDebugMessage(self->at(index));
}

//  QList<QOpenGLDebugMessage>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpenGLDebugMessage(QList<QOpenGLDebugMessage> *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
