//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qstring.h>

//  QTextBlock::QTextBlock()
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZN10QTextBlockC1Ev() {
  return new QTextBlock();
}

//  QTextBlock::QTextBlock(const QTextBlock &o)
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZN10QTextBlockC1ERKS_(const QTextBlock *o) {
  return new QTextBlock(*o);
}

//  bool QTextBlock::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock7isValidEv(const QTextBlock *self) {
  return self->isValid();
}

//  bool QTextBlock::operator==(const QTextBlock &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlockeqERKS_(
    const QTextBlock *self,
    const QTextBlock *o) {
  return self->operator==(*o);
}

//  bool QTextBlock::operator!=(const QTextBlock &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlockneERKS_(
    const QTextBlock *self,
    const QTextBlock *o) {
  return self->operator!=(*o);
}

//  bool QTextBlock::operator<(const QTextBlock &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlockltERKS_(
    const QTextBlock *self,
    const QTextBlock *o) {
  return self->operator<(*o);
}

//  int QTextBlock::position() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock8positionEv(const QTextBlock *self) {
  return self->position();
}

//  int QTextBlock::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock6lengthEv(const QTextBlock *self) {
  return self->length();
}

//  bool QTextBlock::contains(int position) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock8containsEi(
    const QTextBlock *self,
    int position) {
  return self->contains(position);
}

//  QTextLayout *QTextBlock::layout() const
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZNK10QTextBlock6layoutEv(const QTextBlock *self) {
  return self->layout();
}

//  void QTextBlock::clearLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock11clearLayoutEv(QTextBlock *self) {
  self->clearLayout();
}

//  QTextBlockFormat QTextBlock::blockFormat() const
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZNK10QTextBlock11blockFormatEv(
    const QTextBlock *self) {
  return new QTextBlockFormat(self->blockFormat());
}

//  int QTextBlock::blockFormatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock16blockFormatIndexEv(const QTextBlock *self) {
  return self->blockFormatIndex();
}

//  QTextCharFormat QTextBlock::charFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK10QTextBlock10charFormatEv(
    const QTextBlock *self) {
  return new QTextCharFormat(self->charFormat());
}

//  int QTextBlock::charFormatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock15charFormatIndexEv(const QTextBlock *self) {
  return self->charFormatIndex();
}

//  Qt::LayoutDirection QTextBlock::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK10QTextBlock13textDirectionEv(
    const QTextBlock *self) {
  return self->textDirection();
}

//  QString QTextBlock::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTextBlock4textEv(const QTextBlock *self) {
  return new QString(self->text());
}

//  const QTextDocument *QTextBlock::document() const
extern "C" Q_DECL_EXPORT
const QTextDocument *ritual_ZNK10QTextBlock8documentEv(
    const QTextBlock *self) {
  return self->document();
}

//  QTextList *QTextBlock::textList() const
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZNK10QTextBlock8textListEv(const QTextBlock *self) {
  return self->textList();
}

//  QTextBlockUserData *QTextBlock::userData() const
extern "C" Q_DECL_EXPORT
QTextBlockUserData *ritual_ZNK10QTextBlock8userDataEv(
    const QTextBlock *self) {
  return self->userData();
}

//  void QTextBlock::setUserData(QTextBlockUserData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock11setUserDataEP18QTextBlockUserData(
    QTextBlock *self,
    QTextBlockUserData *data) {
  self->setUserData(data);
}

//  int QTextBlock::userState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock9userStateEv(const QTextBlock *self) {
  return self->userState();
}

//  void QTextBlock::setUserState(int state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock12setUserStateEi(QTextBlock *self, int state) {
  self->setUserState(state);
}

//  int QTextBlock::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock8revisionEv(const QTextBlock *self) {
  return self->revision();
}

//  void QTextBlock::setRevision(int rev)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock11setRevisionEi(QTextBlock *self, int rev) {
  self->setRevision(rev);
}

//  bool QTextBlock::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextBlock9isVisibleEv(const QTextBlock *self) {
  return self->isVisible();
}

//  void QTextBlock::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock10setVisibleEb(QTextBlock *self, bool visible) {
  self->setVisible(visible);
}

//  int QTextBlock::blockNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock11blockNumberEv(const QTextBlock *self) {
  return self->blockNumber();
}

//  int QTextBlock::firstLineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock15firstLineNumberEv(const QTextBlock *self) {
  return self->firstLineNumber();
}

//  void QTextBlock::setLineCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlock12setLineCountEi(QTextBlock *self, int count) {
  self->setLineCount(count);
}

//  int QTextBlock::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock9lineCountEv(const QTextBlock *self) {
  return self->lineCount();
}

//  iterator QTextBlock::begin() const
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZNK10QTextBlock5beginEv(
    const QTextBlock *self) {
  return new QTextBlock::iterator(self->begin());
}

//  iterator QTextBlock::end() const
extern "C" Q_DECL_EXPORT
QTextBlock::iterator *ritual_ZNK10QTextBlock3endEv(const QTextBlock *self) {
  return new QTextBlock::iterator(self->end());
}

//  QTextBlock QTextBlock::next() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK10QTextBlock4nextEv(const QTextBlock *self) {
  return new QTextBlock(self->next());
}

//  QTextBlock QTextBlock::previous() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK10QTextBlock8previousEv(const QTextBlock *self) {
  return new QTextBlock(self->previous());
}

//  int QTextBlock::fragmentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextBlock13fragmentIndexEv(const QTextBlock *self) {
  return self->fragmentIndex();
}

//  QTextBlock::~QTextBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextBlockD1Ev(QTextBlock *self) {
  delete self;
}
