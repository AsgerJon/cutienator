//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlist.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlist.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>

//  const QMetaObject *QTextList::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTextList10metaObjectEv(
    const QTextList *self) {
  return self->metaObject();
}

//  QString QTextList::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTextList2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextList::tr(s, c, n));
}

//  QTextList::QTextList(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN9QTextListC1EP13QTextDocument(QTextDocument *doc) {
  return new QTextList(doc);
}

//  QTextList::~QTextList()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextListD1Ev(QTextList *self) {
  delete self;
}

//  int QTextList::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextList5countEv(const QTextList *self) {
  return self->count();
}

//  QTextBlock QTextList::item(int i) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK9QTextList4itemEi(const QTextList *self, int i) {
  return new QTextBlock(self->item(i));
}

//  int QTextList::itemNumber(const QTextBlock &a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextList10itemNumberERK10QTextBlock(
    const QTextList *self,
    const QTextBlock *a0) {
  return self->itemNumber(*a0);
}

//  QString QTextList::itemText(const QTextBlock &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextList8itemTextERK10QTextBlock(
    const QTextList *self,
    const QTextBlock *a0) {
  return new QString(self->itemText(*a0));
}

//  void QTextList::removeItem(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList10removeItemEi(QTextList *self, int i) {
  self->removeItem(i);
}

//  void QTextList::remove(const QTextBlock &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList6removeERK10QTextBlock(
    QTextList *self,
    const QTextBlock *a0) {
  self->remove(*a0);
}

//  void QTextList::add(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList3addERK10QTextBlock(
    QTextList *self,
    const QTextBlock *block) {
  self->add(*block);
}

//  void QTextList::setFormat(const QTextListFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList9setFormatERK15QTextListFormat(
    QTextList *self,
    const QTextListFormat *format) {
  self->setFormat(*format);
}

//  QTextListFormat QTextList::format() const
extern "C" Q_DECL_EXPORT
QTextListFormat *ritual_ZNK9QTextList6formatEv(const QTextList *self) {
  return new QTextListFormat(self->format());
}
