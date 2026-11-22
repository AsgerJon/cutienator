//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpicture.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpicture.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  QPicture::QPicture(int formatVersion)
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZN8QPictureC1Ei(int formatVersion) {
  return new QPicture(formatVersion);
}

//  QPicture::QPicture(const QPicture &a0)
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZN8QPictureC1ERKS_(const QPicture *a0) {
  return new QPicture(*a0);
}

//  QPicture::~QPicture()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPictureD1Ev(QPicture *self) {
  delete self;
}

//  bool QPicture::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPicture6isNullEv(const QPicture *self) {
  return self->isNull();
}

//  int QPicture::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPicture7devTypeEv(const QPicture *self) {
  return self->devType();
}

//  uint QPicture::size() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8QPicture4sizeEv(const QPicture *self) {
  return self->size();
}

//  const char *QPicture::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK8QPicture4dataEv(const QPicture *self) {
  return self->data();
}

//  void QPicture::setData(const char *data, uint size)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture7setDataEPKcj(
    QPicture *self,
    const char *data,
    uint size) {
  self->setData(data, size);
}

//  bool QPicture::play(QPainter *p)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4playEP8QPainter(QPicture *self, QPainter *p) {
  return self->play(p);
}

//  bool QPicture::load(QIODevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4loadEP9QIODevice(QPicture *self, QIODevice *dev) {
  return self->load(dev);
}

//  bool QPicture::load(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4loadERK7QString(
    QPicture *self,
    const QString *fileName) {
  return self->load(*fileName);
}

//  bool QPicture::save(QIODevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4saveEP9QIODevice(QPicture *self, QIODevice *dev) {
  return self->save(dev);
}

//  bool QPicture::save(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4saveERK7QString(
    QPicture *self,
    const QString *fileName) {
  return self->save(*fileName);
}

//  QRect QPicture::boundingRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QPicture12boundingRectEv(const QPicture *self) {
  return new QRect(self->boundingRect());
}

//  void QPicture::setBoundingRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture15setBoundingRectERK5QRect(
    QPicture *self,
    const QRect *r) {
  self->setBoundingRect(*r);
}

//  void QPicture::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture6detachEv(QPicture *self) {
  self->detach();
}

//  bool QPicture::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPicture10isDetachedEv(const QPicture *self) {
  return self->isDetached();
}

//  QPaintEngine *QPicture::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK8QPicture11paintEngineEv(const QPicture *self) {
  return self->paintEngine();
}
