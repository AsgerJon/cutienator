//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlerror.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlerror.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QScxmlError::QScxmlError()
extern "C" Q_DECL_EXPORT
QScxmlError *ritual_ZN11QScxmlErrorC1Ev() {
  return new QScxmlError();
}

//  QScxmlError::QScxmlError(const QString &fileName, int line, int column,
//      const QString &description)
extern "C" Q_DECL_EXPORT
QScxmlError *ritual_ZN11QScxmlErrorC1ERK7QStringiiS2_(
    const QString *fileName,
    int line,
    int column,
    const QString *description) {
  return new QScxmlError(*fileName, line, column, *description);
}

//  QScxmlError::QScxmlError(const QScxmlError &a0)
extern "C" Q_DECL_EXPORT
QScxmlError *ritual_ZN11QScxmlErrorC1ERKS_(const QScxmlError *a0) {
  return new QScxmlError(*a0);
}

//  QScxmlError &QScxmlError::operator=(const QScxmlError &a0)
extern "C" Q_DECL_EXPORT
QScxmlError *ritual_ZN11QScxmlErroraSERKS_(
    QScxmlError *self,
    const QScxmlError *a0) {
  return &(self->operator=(*a0));
}

//  QScxmlError::~QScxmlError()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlErrorD1Ev(QScxmlError *self) {
  delete self;
}

//  bool QScxmlError::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QScxmlError7isValidEv(const QScxmlError *self) {
  return self->isValid();
}

//  QString QScxmlError::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlError8fileNameEv(const QScxmlError *self) {
  return new QString(self->fileName());
}

//  int QScxmlError::line() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QScxmlError4lineEv(const QScxmlError *self) {
  return self->line();
}

//  int QScxmlError::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QScxmlError6columnEv(const QScxmlError *self) {
  return self->column();
}

//  QString QScxmlError::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlError11descriptionEv(const QScxmlError *self) {
  return new QString(self->description());
}

//  QString QScxmlError::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlError8toStringEv(const QScxmlError *self) {
  return new QString(self->toString());
}

//  QList<QScxmlError>::QList()
extern "C" Q_DECL_EXPORT
QList<QScxmlError> *ritual_list_make_QScxmlError() {
  return new QList<QScxmlError>();
}

//  void QList<QScxmlError>::append(const QScxmlError &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScxmlError(
    QList<QScxmlError> *self,
    const QScxmlError *element) {
  self->append(*element);
}

//  qsizetype QList<QScxmlError>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScxmlError(const QList<QScxmlError> *self) {
  return self->size();
}

//  const QScxmlError &QList<QScxmlError>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QScxmlError *ritual_list_at_QScxmlError(
    const QList<QScxmlError> *self,
    long long index) {
  return new QScxmlError(self->at(index));
}

//  QList<QScxmlError>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScxmlError(QList<QScxmlError> *self) {
  delete self;
}
