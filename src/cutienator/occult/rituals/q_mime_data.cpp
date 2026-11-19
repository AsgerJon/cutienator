//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmimedata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmimedata.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QMimeData10metaObjectEv(
    const QMimeData *self) {
  return self->metaObject();
}

//  QString QMimeData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QMimeData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMimeData::tr(s, c, n));
}

//  QMimeData::QMimeData()
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZN9QMimeDataC1Ev() {
  return new QMimeData();
}

//  QMimeData::~QMimeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeDataD1Ev(QMimeData *self) {
  delete self;
}

//  bool QMimeData::hasUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasUrlsEv(const QMimeData *self) {
  return self->hasUrls();
}

//  QString QMimeData::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeData4textEv(const QMimeData *self) {
  return new QString(self->text());
}

//  void QMimeData::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setTextERK7QString(
    QMimeData *self,
    const QString *text) {
  self->setText(*text);
}

//  bool QMimeData::hasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasTextEv(const QMimeData *self) {
  return self->hasText();
}

//  QString QMimeData::html() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeData4htmlEv(const QMimeData *self) {
  return new QString(self->html());
}

//  void QMimeData::setHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setHtmlERK7QString(
    QMimeData *self,
    const QString *html) {
  self->setHtml(*html);
}

//  bool QMimeData::hasHtml() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasHtmlEv(const QMimeData *self) {
  return self->hasHtml();
}

//  QVariant QMimeData::imageData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QMimeData9imageDataEv(const QMimeData *self) {
  return new QVariant(self->imageData());
}

//  void QMimeData::setImageData(const QVariant &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12setImageDataERK8QVariant(
    QMimeData *self,
    const QVariant *image) {
  self->setImageData(*image);
}

//  bool QMimeData::hasImage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData8hasImageEv(const QMimeData *self) {
  return self->hasImage();
}

//  QVariant QMimeData::colorData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QMimeData9colorDataEv(const QMimeData *self) {
  return new QVariant(self->colorData());
}

//  void QMimeData::setColorData(const QVariant &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12setColorDataERK8QVariant(
    QMimeData *self,
    const QVariant *color) {
  self->setColorData(*color);
}

//  bool QMimeData::hasColor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData8hasColorEv(const QMimeData *self) {
  return self->hasColor();
}

//  QByteArray QMimeData::data(const QString &mimetype) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QMimeData4dataERK7QString(
    const QMimeData *self,
    const QString *mimetype) {
  return new QByteArray(self->data(*mimetype));
}

//  void QMimeData::setData(const QString &mimetype, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setDataERK7QStringRK10QByteArray(
    QMimeData *self,
    const QString *mimetype,
    const QByteArray *data) {
  self->setData(*mimetype, *data);
}

//  void QMimeData::removeFormat(const QString &mimetype)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12removeFormatERK7QString(
    QMimeData *self,
    const QString *mimetype) {
  self->removeFormat(*mimetype);
}

//  bool QMimeData::hasFormat(const QString &mimetype) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData9hasFormatERK7QString(
    const QMimeData *self,
    const QString *mimetype) {
  return self->hasFormat(*mimetype);
}

//  void QMimeData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData5clearEv(QMimeData *self) {
  self->clear();
}
