//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>

//  QHashedStringRef::QHashedStringRef()
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1Ev() {
  return new QHashedStringRef();
}

//  QHashedStringRef::QHashedStringRef(const QString &a0)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1ERK7QString(
    const QString *a0) {
  return new QHashedStringRef(*a0);
}

//  QHashedStringRef::QHashedStringRef(QStringView a0)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1E11QStringView(
    const QString *a0) {
  return new QHashedStringRef(QStringView(*a0));
}

//  QHashedStringRef::QHashedStringRef(const QChar *a0, int a1)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1EPK5QChari(
    const QChar *a0,
    int a1) {
  return new QHashedStringRef(a0, a1);
}

//  QHashedStringRef::QHashedStringRef(const QChar *a0, int a1, quint32 a2)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1EPK5QCharij(
    const QChar *a0,
    int a1,
    quint32 a2) {
  return new QHashedStringRef(a0, a1, a2);
}

//  QHashedStringRef::QHashedStringRef(const QHashedString &a0)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1ERK13QHashedString(
    const QHashedString *a0) {
  return new QHashedStringRef(*a0);
}

//  QHashedStringRef::QHashedStringRef(const QHashedStringRef &a0)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefC1ERKS_(
    const QHashedStringRef *a0) {
  return new QHashedStringRef(*a0);
}

//  QHashedStringRef &QHashedStringRef::operator=(const QHashedStringRef &a0)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN16QHashedStringRefaSERKS_(
    QHashedStringRef *self,
    const QHashedStringRef *a0) {
  return &(self->operator=(*a0));
}

//  bool QHashedStringRef::operator==(const QString &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefeqERK7QString(
    const QHashedStringRef *self,
    const QString *string) {
  return self->operator==(*string);
}

//  bool QHashedStringRef::operator==(const QHashedString &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefeqERK13QHashedString(
    const QHashedStringRef *self,
    const QHashedString *string) {
  return self->operator==(*string);
}

//  bool QHashedStringRef::operator==(const QHashedStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefeqERKS_(
    const QHashedStringRef *self,
    const QHashedStringRef *string) {
  return self->operator==(*string);
}

//  bool QHashedStringRef::operator==(const QHashedCStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefeqERK17QHashedCStringRef(
    const QHashedStringRef *self,
    const QHashedCStringRef *string) {
  return self->operator==(*string);
}

//  bool QHashedStringRef::operator!=(const QString &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefneERK7QString(
    const QHashedStringRef *self,
    const QString *string) {
  return self->operator!=(*string);
}

//  bool QHashedStringRef::operator!=(const QHashedString &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefneERK13QHashedString(
    const QHashedStringRef *self,
    const QHashedString *string) {
  return self->operator!=(*string);
}

//  bool QHashedStringRef::operator!=(const QHashedStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefneERKS_(
    const QHashedStringRef *self,
    const QHashedStringRef *string) {
  return self->operator!=(*string);
}

//  bool QHashedStringRef::operator!=(const QHashedCStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRefneERK17QHashedCStringRef(
    const QHashedStringRef *self,
    const QHashedCStringRef *string) {
  return self->operator!=(*string);
}

//  quint32 QHashedStringRef::hash() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QHashedStringRef4hashEv(const QHashedStringRef *self) {
  return self->hash();
}

//  QChar *QHashedStringRef::data()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN16QHashedStringRef4dataEv(QHashedStringRef *self) {
  return self->data();
}

//  const QChar &QHashedStringRef::at(int a0) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK16QHashedStringRef2atEi(
    const QHashedStringRef *self,
    int a0) {
  return new QChar(self->at(a0));
}

//  const QChar *QHashedStringRef::constData() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK16QHashedStringRef9constDataEv(
    const QHashedStringRef *self) {
  return self->constData();
}

//  bool QHashedStringRef::startsWith(const QString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRef10startsWithERK7QString(
    const QHashedStringRef *self,
    const QString *a0) {
  return self->startsWith(*a0);
}

//  bool QHashedStringRef::endsWith(const QString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRef8endsWithERK7QString(
    const QHashedStringRef *self,
    const QString *a0) {
  return self->endsWith(*a0);
}

//  int QHashedStringRef::indexOf(const QChar &a0, int from) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHashedStringRef7indexOfERK5QChari(
    const QHashedStringRef *self,
    const QChar *a0,
    int from) {
  return self->indexOf(*a0, from);
}

//  QHashedStringRef QHashedStringRef::mid(int a0, int a1) const
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZNK16QHashedStringRef3midEii(
    const QHashedStringRef *self,
    int a0,
    int a1) {
  return new QHashedStringRef(self->mid(a0, a1));
}

//  QList<QHashedStringRef> QHashedStringRef::split(const QChar sep) const
extern "C" Q_DECL_EXPORT
QList<QHashedStringRef> *ritual_ZNK16QHashedStringRef5splitE5QChar(
    const QHashedStringRef *self,
    const QChar *sep) {
  return new QList<QHashedStringRef>(self->split(*sep));
}

//  bool QHashedStringRef::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRef7isEmptyEv(const QHashedStringRef *self) {
  return self->isEmpty();
}

//  int QHashedStringRef::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHashedStringRef6lengthEv(const QHashedStringRef *self) {
  return self->length();
}

//  bool QHashedStringRef::startsWithUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRef15startsWithUpperEv(
    const QHashedStringRef *self) {
  return self->startsWithUpper();
}

//  QString QHashedStringRef::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QHashedStringRef8toStringEv(
    const QHashedStringRef *self) {
  return new QString(self->toString());
}

//  bool QHashedStringRef::isLatin1() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHashedStringRef8isLatin1Ev(const QHashedStringRef *self) {
  return self->isLatin1();
}

//  void QHashedStringRef::computeHash() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QHashedStringRef11computeHashEv(
    const QHashedStringRef *self) {
  self->computeHash();
}

//  QHashedStringRef::~QHashedStringRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHashedStringRefD1Ev(QHashedStringRef *self) {
  delete self;
}

//  QList<QHashedStringRef>::QList()
extern "C" Q_DECL_EXPORT
QList<QHashedStringRef> *ritual_list_make_QHashedStringRef() {
  return new QList<QHashedStringRef>();
}

//  void QList<QHashedStringRef>::append(const QHashedStringRef &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHashedStringRef(
    QList<QHashedStringRef> *self,
    const QHashedStringRef *element) {
  self->append(*element);
}

//  qsizetype QList<QHashedStringRef>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHashedStringRef(
    const QList<QHashedStringRef> *self) {
  return self->size();
}

//  const QHashedStringRef &QList<QHashedStringRef>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_list_at_QHashedStringRef(
    const QList<QHashedStringRef> *self,
    long long index) {
  return new QHashedStringRef(self->at(index));
}

//  QList<QHashedStringRef>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHashedStringRef(QList<QHashedStringRef> *self) {
  delete self;
}
