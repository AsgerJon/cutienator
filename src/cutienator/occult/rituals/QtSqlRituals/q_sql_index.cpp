//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlindex.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlindex.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlfield.h>

//  QSqlIndex::QSqlIndex(const QString &cursorName, const QString &name)
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZN9QSqlIndexC1ERK7QStringS2_(
    const QString *cursorName,
    const QString *name) {
  return new QSqlIndex(*cursorName, *name);
}

//  QSqlIndex::QSqlIndex(const QSqlIndex &other)
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZN9QSqlIndexC1ERKS_(const QSqlIndex *other) {
  return new QSqlIndex(*other);
}

//  QSqlIndex::QSqlIndex(QSqlIndex &&other)
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZN9QSqlIndexC1EOS_(QSqlIndex *other) {
  return new QSqlIndex(std::move(*other));
}

//  QSqlIndex::~QSqlIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndexD1Ev(QSqlIndex *self) {
  delete self;
}

//  QSqlIndex &QSqlIndex::operator=(const QSqlIndex &other)
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZN9QSqlIndexaSERKS_(
    QSqlIndex *self,
    const QSqlIndex *other) {
  return &(self->operator=(*other));
}

//  QSqlIndex &QSqlIndex::operator=(QSqlIndex &&other)
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZN9QSqlIndexaSEOS_(QSqlIndex *self, QSqlIndex *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QSqlIndex::swap(QSqlIndex &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex4swapERS_(QSqlIndex *self, QSqlIndex *other) {
  self->swap(*other);
}

//  void QSqlIndex::setCursorName(const QString &cursorName)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex13setCursorNameERK7QString(
    QSqlIndex *self,
    const QString *cursorName) {
  self->setCursorName(*cursorName);
}

//  QString QSqlIndex::cursorName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlIndex10cursorNameEv(const QSqlIndex *self) {
  return new QString(self->cursorName());
}

//  void QSqlIndex::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex7setNameERK7QString(
    QSqlIndex *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QSqlIndex::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlIndex4nameEv(const QSqlIndex *self) {
  return new QString(self->name());
}

//  void QSqlIndex::append(const QSqlField &field)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex6appendERK9QSqlField(
    QSqlIndex *self,
    const QSqlField *field) {
  self->append(*field);
}

//  void QSqlIndex::append(const QSqlField &field, bool desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex6appendERK9QSqlFieldb(
    QSqlIndex *self,
    const QSqlField *field,
    bool desc) {
  self->append(*field, desc);
}

//  bool QSqlIndex::isDescending(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlIndex12isDescendingEi(const QSqlIndex *self, int i) {
  return self->isDescending(i);
}

//  void QSqlIndex::setDescending(int i, bool desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlIndex13setDescendingEib(
    QSqlIndex *self,
    int i,
    bool desc) {
  self->setDescending(i, desc);
}
