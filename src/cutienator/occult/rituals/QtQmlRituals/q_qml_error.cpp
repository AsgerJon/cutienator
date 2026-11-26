//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlerror.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlerror.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QQmlError::QQmlError()
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN9QQmlErrorC1Ev() {
  return new QQmlError();
}

//  QQmlError::QQmlError(const QQmlError &a0)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN9QQmlErrorC1ERKS_(const QQmlError *a0) {
  return new QQmlError(*a0);
}

//  QQmlError::QQmlError(QQmlError &&other)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN9QQmlErrorC1EOS_(QQmlError *other) {
  return new QQmlError(std::move(*other));
}

//  QQmlError &QQmlError::operator=(const QQmlError &a0)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN9QQmlErroraSERKS_(QQmlError *self, const QQmlError *a0) {
  return &(self->operator=(*a0));
}

//  QQmlError &QQmlError::operator=(QQmlError &&other)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN9QQmlErroraSEOS_(QQmlError *self, QQmlError *other) {
  return &(self->operator=(std::move(*other)));
}

//  QQmlError::~QQmlError()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlErrorD1Ev(QQmlError *self) {
  delete self;
}

//  void QQmlError::swap(QQmlError &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError4swapERS_(QQmlError *self, QQmlError *other) {
  self->swap(*other);
}

//  bool QQmlError::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQmlError7isValidEv(const QQmlError *self) {
  return self->isValid();
}

//  QUrl QQmlError::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK9QQmlError3urlEv(const QQmlError *self) {
  return new QUrl(self->url());
}

//  void QQmlError::setUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError6setUrlERK4QUrl(QQmlError *self, const QUrl *a0) {
  self->setUrl(*a0);
}

//  QString QQmlError::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QQmlError11descriptionEv(const QQmlError *self) {
  return new QString(self->description());
}

//  void QQmlError::setDescription(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError14setDescriptionERK7QString(
    QQmlError *self,
    const QString *a0) {
  self->setDescription(*a0);
}

//  int QQmlError::line() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQmlError4lineEv(const QQmlError *self) {
  return self->line();
}

//  void QQmlError::setLine(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError7setLineEi(QQmlError *self, int a0) {
  self->setLine(a0);
}

//  int QQmlError::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQmlError6columnEv(const QQmlError *self) {
  return self->column();
}

//  void QQmlError::setColumn(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError9setColumnEi(QQmlError *self, int a0) {
  self->setColumn(a0);
}

//  QObject *QQmlError::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK9QQmlError6objectEv(const QQmlError *self) {
  return self->object();
}

//  void QQmlError::setObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError9setObjectEP7QObject(QQmlError *self, QObject *a0) {
  self->setObject(a0);
}

//  QtMsgType QQmlError::messageType() const
extern "C" Q_DECL_EXPORT
QtMsgType ritual_ZNK9QQmlError11messageTypeEv(const QQmlError *self) {
  return self->messageType();
}

//  void QQmlError::setMessageType(QtMsgType messageType)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlError14setMessageTypeE9QtMsgType(
    QQmlError *self,
    QtMsgType messageType) {
  self->setMessageType(messageType);
}

//  QString QQmlError::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QQmlError8toStringEv(const QQmlError *self) {
  return new QString(self->toString());
}

//  bool operator==(const QQmlError &a, const QQmlError &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QQmlErrorS1_(const QQmlError *a, const QQmlError *b) {
  return operator==(*a, *b);
}

//  QList<QQmlError>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_list_make_QQmlError() {
  return new QList<QQmlError>();
}

//  void QList<QQmlError>::append(const QQmlError &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlError(
    QList<QQmlError> *self,
    const QQmlError *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlError>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlError(const QList<QQmlError> *self) {
  return self->size();
}

//  const QQmlError &QList<QQmlError>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlError *ritual_list_at_QQmlError(
    const QList<QQmlError> *self,
    long long index) {
  return new QQmlError(self->at(index));
}

//  QList<QQmlError>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlError(QList<QQmlError> *self) {
  delete self;
}
