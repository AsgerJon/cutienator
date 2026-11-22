//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>

//  QTextFrame::iterator::iterator()
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZN10QTextFrame8iteratorC1Ev() {
  return new QTextFrame::iterator();
}

//  QTextFrame *QTextFrame::iterator::parentFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK10QTextFrame8iterator11parentFrameEv(
    const QTextFrame::iterator *self) {
  return self->parentFrame();
}

//  QTextFrame *QTextFrame::iterator::currentFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK10QTextFrame8iterator12currentFrameEv(
    const QTextFrame::iterator *self) {
  return self->currentFrame();
}

//  QTextBlock QTextFrame::iterator::currentBlock() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK10QTextFrame8iterator12currentBlockEv(
    const QTextFrame::iterator *self) {
  return new QTextBlock(self->currentBlock());
}

//  bool QTextFrame::iterator::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextFrame8iterator5atEndEv(
    const QTextFrame::iterator *self) {
  return self->atEnd();
}

//  bool QTextFrame::iterator::operator==(const iterator &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextFrame8iteratoreqERKS0_(
    const QTextFrame::iterator *self,
    const QTextFrame::iterator *o) {
  return self->operator==(*o);
}

//  bool QTextFrame::iterator::operator!=(const iterator &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextFrame8iteratorneERKS0_(
    const QTextFrame::iterator *self,
    const QTextFrame::iterator *o) {
  return self->operator!=(*o);
}

//  iterator QTextFrame::iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZN10QTextFrame8iteratorppEi(
    QTextFrame::iterator *self,
    int a0) {
  return new QTextFrame::iterator(self->operator++(a0));
}

//  iterator QTextFrame::iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZN10QTextFrame8iteratormmEi(
    QTextFrame::iterator *self,
    int a0) {
  return new QTextFrame::iterator(self->operator--(a0));
}

//  QTextFrame::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrame8iteratorD1Ev(QTextFrame::iterator *self) {
  delete self;
}
