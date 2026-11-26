//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qpaintedtextureimage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qpaintedtextureimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qpaintedtextureimage.h>
#include <Qt3DRender/private/qpaintedtextureimage_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/qimage.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/texture/qpaintedtextureimage.cpp, line 207, as _ZN10Qt3DRender33QPaintedTextureImageDataGeneratorC1ERK6QImageiN8Qt3DCore7QNodeIdE
namespace Qt3DRender {
inline QPaintedTextureImageDataGenerator::QPaintedTextureImageDataGenerator(const QImage &image, int gen, Qt3DCore::QNodeId texId)
    : m_image(image)    // pixels are implicitly shared, no copying
    , m_generation(gen)
    , m_paintedTextureImageId(texId)
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qpaintedtextureimage.cpp, line 214, as _ZN10Qt3DRender33QPaintedTextureImageDataGeneratorD1Ev
namespace Qt3DRender {
inline QPaintedTextureImageDataGenerator::~QPaintedTextureImageDataGenerator()
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qpaintedtextureimage.cpp, line 218, as _ZN10Qt3DRender33QPaintedTextureImageDataGeneratorclEv
namespace Qt3DRender {
inline QTextureImageDataPtr QPaintedTextureImageDataGenerator::operator ()()
{
    QTextureImageDataPtr textureData = QTextureImageDataPtr::create();
    textureData->setImage(m_image);
    return textureData;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qpaintedtextureimage.cpp, line 225, as _ZNK10Qt3DRender33QPaintedTextureImageDataGeneratoreqERKNS_26QTextureImageDataGeneratorE
namespace Qt3DRender {
inline bool QPaintedTextureImageDataGenerator::operator ==(const QTextureImageDataGenerator &other) const
{
    const QPaintedTextureImageDataGenerator *otherFunctor = functor_cast<QPaintedTextureImageDataGenerator>(&other);
    return (otherFunctor != nullptr && otherFunctor->m_generation == m_generation && otherFunctor->m_paintedTextureImageId == m_paintedTextureImageId);
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QPaintedTextureImageDataGenerator that Python can take functions over in. Every Qt3DRender::QPaintedTextureImageDataGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0)(const void *, int *);
class CuteQt3DRender_QPaintedTextureImageDataGenerator : public Qt3DRender::QPaintedTextureImageDataGenerator {
public:
  using Qt3DRender::QPaintedTextureImageDataGenerator::QPaintedTextureImageDataGenerator;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::QPaintedTextureImageDataGenerator::id();
  }
};

//  Qt3DRender::QPaintedTextureImageDataGenerator::QPaintedTextureImageDataGe
//      nerator(const QImage &image, int gen, Qt3DCore::QNodeId texId)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPaintedTextureImageDataGenerator *ritual_ZN10Qt3DRender33QPaintedTextureImageDataGeneratorC1ERK6QImageiN8Qt3DCore7QNodeIdE(
    const QImage *image,
    int gen,
    const Qt3DCore::QNodeId *texId) {
  return new CuteQt3DRender_QPaintedTextureImageDataGenerator(
      *image,
      gen,
      *texId);
}

//  Qt3DRender::QPaintedTextureImageDataGenerator::~QPaintedTextureImageDataG
//      enerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender33QPaintedTextureImageDataGeneratorD1Ev(
    Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  delete self;
}

//  QTextureImageDataPtr
//      Qt3DRender::QPaintedTextureImageDataGenerator::operator()()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataPtr *ritual_ZN10Qt3DRender33QPaintedTextureImageDataGeneratorclEv(
    Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  return new Qt3DRender::QTextureImageDataPtr(self->operator()());
}

//  bool Qt3DRender::QPaintedTextureImageDataGenerator::operator==(const
//      QTextureImageDataGenerator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender33QPaintedTextureImageDataGeneratoreqERKNS_26QTextureImageDataGeneratorE(
    const Qt3DRender::QPaintedTextureImageDataGenerator *self,
    const Qt3DRender::QTextureImageDataGenerator *other) {
  return self->operator==(*other);
}

//  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2idEv(
    const Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  return self->id();
}

//  a Python function taken by a
//      CuteQt3DRender_QPaintedTextureImageDataGenerator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPaintedTextureImageDataGenerator(
    Qt3DRender::QPaintedTextureImageDataGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPaintedTextureImageDataGenerator *>(self)->take(key, call);
}

//  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2idEv(
    const Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  return self->Qt3DRender::QPaintedTextureImageDataGenerator::id();
}

//  a Qt3DRender::QTextureImageDataPtr a ritual of
//      Qt3DRender::QPaintedTextureImageDataGenerator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QPaintedTextureImageDataGenerator__Qt3DRender_QTextureImageDataPtr(
    Qt3DRender::QTextureImageDataPtr *self) {
  delete self;
}
