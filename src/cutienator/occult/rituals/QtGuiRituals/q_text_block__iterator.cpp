//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>

//  QTextBlock::iterator::iterator(const QTextDocumentPrivate *priv, int
//      begin, int end, int f)
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratorC1EPK20QTextDocumentPrivateiii(
    const QTextDocumentPrivate *priv,
    int begin,
    int end,
    int f) {
  return new QTextBlock::iterator(priv, begin, end, f);
}

//  QTextBlock::iterator::iterator()
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratorC1Ev() {
  return new QTextBlock::iterator();
}

//  QTextFragment QTextBlock::iterator::fragment() const
extern "C" Q_DECL_EXPORT
QTextFragment *ritual_ZNK10QTextBlock8iterator8fragmentEv(
    const QTextBlock::iterator *self) {
  return new QTextFragment(self->fragment());
}

//  bool QTextBlock::iterator::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock8iterator5atEndEv(
    const QTextBlock::iterator *self) {
  return self->atEnd();
}

//  bool QTextBlock::iterator::operator==(const iterator &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock8iteratoreqERKS0_(
    const QTextBlock::iterator *self,
    const QTextBlock::iterator *o) {
  return self->operator==(*o);
}

//  bool QTextBlock::iterator::operator!=(const iterator &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock8iteratorneERKS0_(
    const QTextBlock::iterator *self,
    const QTextBlock::iterator *o) {
  return self->operator!=(*o);
}

//  iterator &QTextBlock::iterator::operator++()
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratorppEv(
    QTextBlock::iterator *self) {
  return &(self->operator++());
}

//  iterator QTextBlock::iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratorppEi(
    QTextBlock::iterator *self,
    int a0) {
  return new QTextBlock::iterator(self->operator++(a0));
}

//  iterator &QTextBlock::iterator::operator--()
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratormmEv(
    QTextBlock::iterator *self) {
  return &(self->operator--());
}

//  iterator QTextBlock::iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZN10QTextBlock8iteratormmEi(
    QTextBlock::iterator *self,
    int a0) {
  return new QTextBlock::iterator(self->operator--(a0));
}

//  QTextBlock::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock8iteratorD1Ev(QTextBlock::iterator *self) {
  delete self;
}
