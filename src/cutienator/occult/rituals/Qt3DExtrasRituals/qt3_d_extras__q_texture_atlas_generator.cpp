//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/qtextureatlas_p.h>
#include <Qt3DExtras/private/qtextureatlas_p_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qabstracttextureimage.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 108, as _ZN10Qt3DExtras22QTextureAtlasGeneratorD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasGenerator::~QTextureAtlasGenerator()
{
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QTextureAtlasGenerator that Python can take functions over in. Every Qt3DExtras::QTextureAtlasGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DExtras_QTextureAtlasGeneratorCall0)(const void *, int *);
class CuteQt3DExtras_QTextureAtlasGenerator : public Qt3DExtras::QTextureAtlasGenerator {
public:
  using Qt3DExtras::QTextureAtlasGenerator::QTextureAtlasGenerator;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasGeneratorCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DExtras::QTextureAtlasGenerator::id();
  }
};

//  Qt3DExtras::QTextureAtlasGenerator::~QTextureAtlasGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QTextureAtlasGeneratorD1Ev(
    Qt3DExtras::QTextureAtlasGenerator *self) {
  delete self;
}

//  Qt3DRender::QTextureDataPtr
//      Qt3DExtras::QTextureAtlasGenerator::operator()()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataPtr *ritual_ZN10Qt3DExtras22QTextureAtlasGeneratorclEv(
    Qt3DExtras::QTextureAtlasGenerator *self) {
  return new Qt3DRender::QTextureDataPtr(self->operator()());
}

//  bool Qt3DExtras::QTextureAtlasGenerator::operator==(const
//      QTextureGenerator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QTextureAtlasGeneratoreqERKN10Qt3DRender17QTextureGeneratorE(
    const Qt3DExtras::QTextureAtlasGenerator *self,
    const Qt3DRender::QTextureGenerator *other) {
  return self->operator==(*other);
}

//  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv(
    const Qt3DExtras::QTextureAtlasGenerator *self) {
  return self->id();
}

//  a Python function taken by a CuteQt3DExtras_QTextureAtlasGenerator, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureAtlasGenerator(
    Qt3DExtras::QTextureAtlasGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureAtlasGenerator *>(self)->take(key, call);
}

//  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv(
    const Qt3DExtras::QTextureAtlasGenerator *self) {
  return self->Qt3DExtras::QTextureAtlasGenerator::id();
}

//  a Qt3DRender::QTextureDataPtr a ritual of
//      Qt3DExtras::QTextureAtlasGenerator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_QTextureAtlasGenerator__Qt3DRender_QTextureDataPtr(
    Qt3DRender::QTextureDataPtr *self) {
  delete self;
}
