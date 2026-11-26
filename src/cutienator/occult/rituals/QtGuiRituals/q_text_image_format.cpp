//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/qstring.h>

//  QTextImageFormat::QTextImageFormat()
extern "C" Q_DECL_EXPORT
QTextImageFormat *ritual_ZN16QTextImageFormatC1Ev() {
  return new QTextImageFormat();
}

//  bool QTextImageFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextImageFormat7isValidEv(const QTextImageFormat *self) {
  return self->isValid();
}

//  void QTextImageFormat::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat7setNameERK7QString(
    QTextImageFormat *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QTextImageFormat::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTextImageFormat4nameEv(const QTextImageFormat *self) {
  return new QString(self->name());
}

//  void QTextImageFormat::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat8setWidthEd(
    QTextImageFormat *self,
    qreal width) {
  self->setWidth(width);
}

//  qreal QTextImageFormat::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextImageFormat5widthEv(const QTextImageFormat *self) {
  return self->width();
}

//  void QTextImageFormat::setMaximumWidth(QTextLength maxWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat15setMaximumWidthE11QTextLength(
    QTextImageFormat *self,
    const QTextLength *maxWidth) {
  self->setMaximumWidth(*maxWidth);
}

//  QTextLength QTextImageFormat::maximumWidth() const
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZNK16QTextImageFormat12maximumWidthEv(
    const QTextImageFormat *self) {
  return new QTextLength(self->maximumWidth());
}

//  void QTextImageFormat::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat9setHeightEd(
    QTextImageFormat *self,
    qreal height) {
  self->setHeight(height);
}

//  qreal QTextImageFormat::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextImageFormat6heightEv(const QTextImageFormat *self) {
  return self->height();
}

//  void QTextImageFormat::setQuality(int quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat10setQualityEi(
    QTextImageFormat *self,
    int quality) {
  self->setQuality(quality);
}

#if QT_DEPRECATED_SINCE(6, 3)
//  void QTextImageFormat::setQuality()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormat10setQualityEv(QTextImageFormat *self) {
  self->setQuality();
}
#endif  // QT_DEPRECATED_SINCE(6, 3)

//  int QTextImageFormat::quality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextImageFormat7qualityEv(const QTextImageFormat *self) {
  return self->quality();
}

//  QTextImageFormat::QTextImageFormat(const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QTextImageFormat *ritual_ZN16QTextImageFormatC1ERK11QTextFormat(
    const QTextFormat *format) {
  return new QTextImageFormat(*format);
}

//  QDataStream &operator<<(QDataStream &a0, const QTextListFormat &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK15QTextListFormat(
    QDataStream *a0,
    const QTextListFormat *a1) {
  return &(operator<<(*a0, *a1));
}

//  QDataStream &operator>>(QDataStream &a0, QTextListFormat &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR15QTextListFormat(
    QDataStream *a0,
    QTextListFormat *a1) {
  return &(operator>>(*a0, *a1));
}

//  QTextImageFormat::~QTextImageFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextImageFormatD1Ev(QTextImageFormat *self) {
  delete self;
}
