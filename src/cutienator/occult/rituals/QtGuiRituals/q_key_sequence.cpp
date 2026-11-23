//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qkeysequence.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qkeysequence.h>
#include <QtCore/qstring.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QKeySequence::QKeySequence()
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1Ev() {
  return new QKeySequence();
}

//  QKeySequence::QKeySequence(const QString &key, SequenceFormat format)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1ERK7QStringNS_14SequenceFormatE(
    const QString *key,
    QKeySequence::SequenceFormat format) {
  return new QKeySequence(*key, format);
}

//  QKeySequence::QKeySequence(int k1, int k2, int k3, int k4)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1Eiiii(
    int k1,
    int k2,
    int k3,
    int k4) {
  return new QKeySequence(k1, k2, k3, k4);
}

//  QKeySequence::QKeySequence(QKeyCombination k1, QKeyCombination k2,
//      QKeyCombination k3, QKeyCombination k4)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1E15QKeyCombinationS0_S0_S0_(
    const QKeyCombination *k1,
    const QKeyCombination *k2,
    const QKeyCombination *k3,
    const QKeyCombination *k4) {
  return new QKeySequence(*k1, *k2, *k3, *k4);
}

//  QKeySequence::QKeySequence(const QKeySequence &ks)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1ERKS_(const QKeySequence *ks) {
  return new QKeySequence(*ks);
}

//  QKeySequence::QKeySequence(StandardKey key)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequenceC1ENS_11StandardKeyE(
    QKeySequence::StandardKey key) {
  return new QKeySequence(key);
}

//  QKeySequence::~QKeySequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QKeySequenceD1Ev(QKeySequence *self) {
  delete self;
}

//  int QKeySequence::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QKeySequence5countEv(const QKeySequence *self) {
  return self->count();
}

//  bool QKeySequence::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequence7isEmptyEv(const QKeySequence *self) {
  return self->isEmpty();
}

//  QString QKeySequence::toString(SequenceFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QKeySequence8toStringENS_14SequenceFormatE(
    const QKeySequence *self,
    QKeySequence::SequenceFormat format) {
  return new QString(self->toString(format));
}

//  QKeySequence QKeySequence::fromString(const QString &str, SequenceFormat
//      format)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequence10fromStringERK7QStringNS_14SequenceFormatE(
    const QString *str,
    QKeySequence::SequenceFormat format) {
  return new QKeySequence(QKeySequence::fromString(*str, format));
}

//  QList<QKeySequence> QKeySequence::listFromString(const QString &str,
//      SequenceFormat format)
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZN12QKeySequence14listFromStringERK7QStringNS_14SequenceFormatE(
    const QString *str,
    QKeySequence::SequenceFormat format) {
  return new QList<QKeySequence>(QKeySequence::listFromString(*str, format));
}

//  QString QKeySequence::listToString(const QList<QKeySequence> &list,
//      SequenceFormat format)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QKeySequence12listToStringERK5QListIS_ENS_14SequenceFormatE(
    const QList<QKeySequence> *list,
    QKeySequence::SequenceFormat format) {
  return new QString(QKeySequence::listToString(*list, format));
}

//  SequenceMatch QKeySequence::matches(const QKeySequence &seq) const
extern "C" Q_DECL_EXPORT
QKeySequence::SequenceMatch ritual_ZNK12QKeySequence7matchesERKS_(
    const QKeySequence *self,
    const QKeySequence *seq) {
  return self->matches(*seq);
}

//  QKeySequence QKeySequence::mnemonic(const QString &text)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN12QKeySequence8mnemonicERK7QString(
    const QString *text) {
  return new QKeySequence(QKeySequence::mnemonic(*text));
}

//  QList<QKeySequence> QKeySequence::keyBindings(StandardKey key)
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZN12QKeySequence11keyBindingsENS_11StandardKeyE(
    QKeySequence::StandardKey key) {
  return new QList<QKeySequence>(QKeySequence::keyBindings(key));
}

//  QVariant QKeySequence::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QKeySequencecv8QVariantEv(const QKeySequence *self) {
  return new QVariant(self->operator QVariant());
}

//  QKeyCombination QKeySequence::operator[](uint i) const
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZNK12QKeySequenceixEj(
    const QKeySequence *self,
    uint i) {
  return new QKeyCombination(self->operator[](i));
}

//  bool QKeySequence::operator==(const QKeySequence &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequenceeqERKS_(
    const QKeySequence *self,
    const QKeySequence *other) {
  return self->operator==(*other);
}

//  bool QKeySequence::operator!=(const QKeySequence &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequenceneERKS_(
    const QKeySequence *self,
    const QKeySequence *other) {
  return self->operator!=(*other);
}

//  bool QKeySequence::operator<(const QKeySequence &ks) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequenceltERKS_(
    const QKeySequence *self,
    const QKeySequence *ks) {
  return self->operator<(*ks);
}

//  bool QKeySequence::operator>(const QKeySequence &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequencegtERKS_(
    const QKeySequence *self,
    const QKeySequence *other) {
  return self->operator>(*other);
}

//  bool QKeySequence::operator<=(const QKeySequence &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequenceleERKS_(
    const QKeySequence *self,
    const QKeySequence *other) {
  return self->operator<=(*other);
}

//  bool QKeySequence::operator>=(const QKeySequence &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequencegeERKS_(
    const QKeySequence *self,
    const QKeySequence *other) {
  return self->operator>=(*other);
}

//  bool QKeySequence::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QKeySequence10isDetachedEv(const QKeySequence *self) {
  return self->isDetached();
}

//  int QKeySequence::assign(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QKeySequence6assignERK7QString(
    QKeySequence *self,
    const QString *str) {
  return self->assign(*str);
}

//  int QKeySequence::assign(const QString &str, SequenceFormat format)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QKeySequence6assignERK7QStringNS_14SequenceFormatE(
    QKeySequence *self,
    const QString *str,
    QKeySequence::SequenceFormat format) {
  return self->assign(*str, format);
}

//  void QKeySequence::setKey(QKeyCombination key, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QKeySequence6setKeyE15QKeyCombinationi(
    QKeySequence *self,
    const QKeyCombination *key,
    int index) {
  self->setKey(*key, index);
}

//  QList<QKeySequence>::QList()
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_list_make_QKeySequence() {
  return new QList<QKeySequence>();
}

//  void QList<QKeySequence>::append(const QKeySequence &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QKeySequence(
    QList<QKeySequence> *self,
    const QKeySequence *element) {
  self->append(*element);
}

//  qsizetype QList<QKeySequence>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QKeySequence(const QList<QKeySequence> *self) {
  return self->size();
}

//  const QKeySequence &QList<QKeySequence>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_list_at_QKeySequence(
    const QList<QKeySequence> *self,
    long long index) {
  return new QKeySequence(self->at(index));
}

//  QList<QKeySequence>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QKeySequence(QList<QKeySequence> *self) {
  delete self;
}
