//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqtttopicname.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqtttopicname.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qlist.h>

//  QMqttTopicName::QMqttTopicName(const QString &name)
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZN14QMqttTopicNameC1ERK7QString(const QString *name) {
  return new QMqttTopicName(*name);
}

//  QMqttTopicName::QMqttTopicName(const QLatin1String &name)
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZN14QMqttTopicNameC1ERK13QLatin1String(
    const QLatin1String *name) {
  return new QMqttTopicName(*name);
}

//  QMqttTopicName::QMqttTopicName(const QMqttTopicName &name)
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZN14QMqttTopicNameC1ERKS_(
    const QMqttTopicName *name) {
  return new QMqttTopicName(*name);
}

//  QMqttTopicName::~QMqttTopicName()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMqttTopicNameD1Ev(QMqttTopicName *self) {
  delete self;
}

//  QMqttTopicName &QMqttTopicName::operator=(const QMqttTopicName &name)
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZN14QMqttTopicNameaSERKS_(
    QMqttTopicName *self,
    const QMqttTopicName *name) {
  return &(self->operator=(*name));
}

#if defined(Q_COMPILER_RVALUE_REFS)
//  QMqttTopicName &QMqttTopicName::operator=(QMqttTopicName &&other)
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZN14QMqttTopicNameaSEOS_(
    QMqttTopicName *self,
    QMqttTopicName *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // defined(Q_COMPILER_RVALUE_REFS)

//  void QMqttTopicName::swap(QMqttTopicName &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMqttTopicName4swapERS_(
    QMqttTopicName *self,
    QMqttTopicName *other) {
  self->swap(*other);
}

//  QString QMqttTopicName::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QMqttTopicName4nameEv(const QMqttTopicName *self) {
  return new QString(self->name());
}

//  void QMqttTopicName::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMqttTopicName7setNameERK7QString(
    QMqttTopicName *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QMqttTopicName::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMqttTopicName7isValidEv(const QMqttTopicName *self) {
  return self->isValid();
}

//  int QMqttTopicName::levelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMqttTopicName10levelCountEv(const QMqttTopicName *self) {
  return self->levelCount();
}

//  QStringList QMqttTopicName::levels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QMqttTopicName6levelsEv(
    const QMqttTopicName *self) {
  return new QList<QString>(self->levels());
}

//  bool operator==(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QMqttTopicNameS1_(
    const QMqttTopicName *lhs,
    const QMqttTopicName *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QMqttTopicNameS1_(
    const QMqttTopicName *lhs,
    const QMqttTopicName *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QMqttTopicNameS1_(
    const QMqttTopicName *lhs,
    const QMqttTopicName *rhs) {
  return operator<(*lhs, *rhs);
}
