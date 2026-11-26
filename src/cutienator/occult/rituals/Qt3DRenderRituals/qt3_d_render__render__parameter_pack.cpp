//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/parameterpack_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/parameterpack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/parameterpack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 11, as _ZN10Qt3DRender6Render13ParameterPackC1Ev
namespace Qt3DRender::Render {
inline ParameterPack::ParameterPack()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 15, as _ZN10Qt3DRender6Render13ParameterPackD1Ev
namespace Qt3DRender::Render {
inline ParameterPack::~ParameterPack()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 19, as _ZN10Qt3DRender6Render13ParameterPack5clearEv
namespace Qt3DRender::Render {
inline void ParameterPack::clear()
{
    m_peers.clear();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 24, as _ZN10Qt3DRender6Render13ParameterPack15appendParameterEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
inline void ParameterPack::appendParameter(Qt3DCore::QNodeId parameterId)
{
    if (!m_peers.contains(parameterId)) {
        m_peers.append(parameterId);
    }
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 31, as _ZN10Qt3DRender6Render13ParameterPack15removeParameterEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
inline void ParameterPack::removeParameter(Qt3DCore::QNodeId parameterId)
{
    m_peers.removeOne(parameterId);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/parameterpack.cpp, line 36, as _ZNK10Qt3DRender6Render13ParameterPack10parametersEv
namespace Qt3DRender::Render {
inline QList<Qt3DCore::QNodeId> ParameterPack::parameters() const
{
    return m_peers;
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::ParameterPack::ParameterPack()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ParameterPack *ritual_ZN10Qt3DRender6Render13ParameterPackC1Ev() {
  return new Qt3DRender::Render::ParameterPack();
}

//  Qt3DRender::Render::ParameterPack::~ParameterPack()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterPackD1Ev(
    Qt3DRender::Render::ParameterPack *self) {
  delete self;
}

//  void Qt3DRender::Render::ParameterPack::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterPack5clearEv(
    Qt3DRender::Render::ParameterPack *self) {
  self->clear();
}

//  void Qt3DRender::Render::ParameterPack::appendParameter(Qt3DCore::QNodeId
//      parameterId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterPack15appendParameterEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::ParameterPack *self,
    const Qt3DCore::QNodeId *parameterId) {
  self->appendParameter(*parameterId);
}

//  void Qt3DRender::Render::ParameterPack::removeParameter(Qt3DCore::QNodeId
//      parameterId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterPack15removeParameterEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::ParameterPack *self,
    const Qt3DCore::QNodeId *parameterId) {
  self->removeParameter(*parameterId);
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::ParameterPack::parameters()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render13ParameterPack10parametersEv(
    const Qt3DRender::Render::ParameterPack *self) {
  return new QList<Qt3DCore::QNodeId>(self->parameters());
}

//  void Qt3DRender::Render::ParameterPack::setParameters(const
//      Qt3DCore::QNodeIdVector &parameterIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterPack13setParametersERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::ParameterPack *self,
    const Qt3DCore::QNodeIdVector *parameterIds) {
  self->setParameters(*parameterIds);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::ParameterPack
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_ParameterPack__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
