//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlabel.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlabel.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpicture.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QLabel10metaObjectEv(const QLabel *self) {
  return self->metaObject();
}

//  QString QLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QLabel2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLabel::tr(s, c, n));
}

//  QLabel::QLabel(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QLabel *ritual_ZN6QLabelC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QLabel(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QLabel::QLabel(const QString &text, QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QLabel *ritual_ZN6QLabelC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *text,
    QWidget *parent,
    int f) {
  return new QLabel(*text, parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QLabel::~QLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabelD1Ev(QLabel *self) {
  delete self;
}

//  QString QLabel::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QLabel4textEv(const QLabel *self) {
  return new QString(self->text());
}

//  QPixmap QLabel::pixmap(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QLabel6pixmapEN2Qt21ReturnByValueConstantE(
    const QLabel *self,
    Qt::ReturnByValueConstant a0) {
  return new QPixmap(self->pixmap(a0));
}

//  QPixmap QLabel::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QLabel6pixmapEv(const QLabel *self) {
  return new QPixmap(self->pixmap());
}

//  QPicture QLabel::picture(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZNK6QLabel7pictureEN2Qt21ReturnByValueConstantE(
    const QLabel *self,
    Qt::ReturnByValueConstant a0) {
  return new QPicture(self->picture(a0));
}

//  QPicture QLabel::picture() const
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZNK6QLabel7pictureEv(const QLabel *self) {
  return new QPicture(self->picture());
}

//  QMovie *QLabel::movie() const
extern "C" Q_DECL_EXPORT
QMovie *ritual_ZNK6QLabel5movieEv(const QLabel *self) {
  return self->movie();
}

//  Qt::TextFormat QLabel::textFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK6QLabel10textFormatEv(const QLabel *self) {
  return self->textFormat();
}

//  void QLabel::setTextFormat(Qt::TextFormat a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel13setTextFormatEN2Qt10TextFormatE(
    QLabel *self,
    Qt::TextFormat a0) {
  self->setTextFormat(a0);
}

//  Qt::Alignment QLabel::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel9alignmentEv(const QLabel *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLabel::setAlignment(Qt::Alignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLabel *self,
    int a0) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a0));
}

//  void QLabel::setWordWrap(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel11setWordWrapEb(QLabel *self, bool on) {
  self->setWordWrap(on);
}

//  bool QLabel::wordWrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel8wordWrapEv(const QLabel *self) {
  return self->wordWrap();
}

//  int QLabel::indent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel6indentEv(const QLabel *self) {
  return self->indent();
}

//  void QLabel::setIndent(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setIndentEi(QLabel *self, int a0) {
  self->setIndent(a0);
}

//  int QLabel::margin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel6marginEv(const QLabel *self) {
  return self->margin();
}

//  void QLabel::setMargin(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setMarginEi(QLabel *self, int a0) {
  self->setMargin(a0);
}

//  bool QLabel::hasScaledContents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel17hasScaledContentsEv(const QLabel *self) {
  return self->hasScaledContents();
}

//  void QLabel::setScaledContents(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel17setScaledContentsEb(QLabel *self, bool a0) {
  self->setScaledContents(a0);
}

//  QSize QLabel::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QLabel8sizeHintEv(const QLabel *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLabel::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QLabel15minimumSizeHintEv(const QLabel *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QLabel::setBuddy(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel8setBuddyEP7QWidget(QLabel *self, QWidget *a0) {
  self->setBuddy(a0);
}

//  QWidget *QLabel::buddy() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK6QLabel5buddyEv(const QLabel *self) {
  return self->buddy();
}

//  int QLabel::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel14heightForWidthEi(const QLabel *self, int a0) {
  return self->heightForWidth(a0);
}

//  bool QLabel::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel17openExternalLinksEv(const QLabel *self) {
  return self->openExternalLinks();
}

//  void QLabel::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel20setOpenExternalLinksEb(QLabel *self, bool open) {
  self->setOpenExternalLinks(open);
}

//  void QLabel::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QLabel *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QLabel::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel20textInteractionFlagsEv(const QLabel *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QLabel::setSelection(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel12setSelectionEii(QLabel *self, int a0, int a1) {
  self->setSelection(a0, a1);
}

//  bool QLabel::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel15hasSelectedTextEv(const QLabel *self) {
  return self->hasSelectedText();
}

//  QString QLabel::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QLabel12selectedTextEv(const QLabel *self) {
  return new QString(self->selectedText());
}

//  int QLabel::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel14selectionStartEv(const QLabel *self) {
  return self->selectionStart();
}

//  void QLabel::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel7setTextERK7QString(QLabel *self, const QString *a0) {
  self->setText(*a0);
}

//  void QLabel::setPixmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setPixmapERK7QPixmap(QLabel *self, const QPixmap *a0) {
  self->setPixmap(*a0);
}

//  void QLabel::setPicture(const QPicture &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel10setPictureERK8QPicture(
    QLabel *self,
    const QPicture *a0) {
  self->setPicture(*a0);
}

//  void QLabel::setMovie(QMovie *movie)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel8setMovieEP6QMovie(QLabel *self, QMovie *movie) {
  self->setMovie(movie);
}

//  void QLabel::setNum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel6setNumEi(QLabel *self, int a0) {
  self->setNum(a0);
}

//  void QLabel::setNum(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel6setNumEd(QLabel *self, double a0) {
  self->setNum(a0);
}

//  void QLabel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel5clearEv(QLabel *self) {
  self->clear();
}
