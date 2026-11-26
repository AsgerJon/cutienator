//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottietextlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietextlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QLottieTextLayer::QLottieTextLayer()
extern "C" Q_DECL_EXPORT
QLottieTextLayer *ritual_ZN16QLottieTextLayerC1Ev() {
  return new QLottieTextLayer();
}

//  QLottieTextLayer::QLottieTextLayer(const QLottieTextLayer &other)
extern "C" Q_DECL_EXPORT
QLottieTextLayer *ritual_ZN16QLottieTextLayerC1ERKS_(
    const QLottieTextLayer *other) {
  return new QLottieTextLayer(*other);
}

//  QLottieBase *QLottieTextLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK16QLottieTextLayer5cloneEv(
    const QLottieTextLayer *self) {
  return self->clone();
}

//  void QLottieTextLayer::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QLottieTextLayer6renderER15QLottieRenderer(
    const QLottieTextLayer *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  int QLottieTextLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QLottieTextLayer5parseERK11QJsonObject(
    QLottieTextLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  const TextDocument &QLottieTextLayer::textDocument() const
extern "C" Q_DECL_EXPORT
QLottieTextLayer::TextDocument *ritual_ZNK16QLottieTextLayer12textDocumentEv(
    const QLottieTextLayer *self) {
  return new QLottieTextLayer::TextDocument(self->textDocument());
}

//  void QLottieTextLayer::setCharData(const QMap<QString, QJsonObject>
//      &chars)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieTextLayer11setCharDataERK4QMapI7QString11QJsonObjectE(
    QLottieTextLayer *self,
    const QMap<QString, QJsonObject> *chars) {
  self->setCharData(*chars);
}

//  QList<QPainterPath> QLottieTextLayer::buildGlyphPaths() const
extern "C" Q_DECL_EXPORT
QList<QPainterPath> *ritual_ZNK16QLottieTextLayer15buildGlyphPathsEv(
    const QLottieTextLayer *self) {
  return new QList<QPainterPath>(self->buildGlyphPaths());
}

//  QLottieTextLayer::~QLottieTextLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieTextLayerD1Ev(QLottieTextLayer *self) {
  delete self;
}

//  QLottieBase *QLottieTextLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK16QLottieTextLayer5cloneEv(
    const QLottieTextLayer *self) {
  return self->QLottieTextLayer::clone();
}

//  int QLottieTextLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN16QLottieTextLayer5parseERK11QJsonObject(
    QLottieTextLayer *self,
    const QJsonObject *definition) {
  return self->QLottieTextLayer::parse(*definition);
}
