//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/coresettings_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/coresettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/coresettings_p.h>
#include <Qt3DCore/private/qcoreaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/aspect/coresettings.cpp, line 29, as _ZN8Qt3DCore19CoreSettingsFunctorC1EPNS_11QCoreAspectE
namespace Qt3DCore {
inline CoreSettingsFunctor::CoreSettingsFunctor(QCoreAspect *aspect)
    : m_aspect(aspect)
    , m_settings(nullptr)
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/aspect/coresettings.cpp, line 35, as _ZNK8Qt3DCore19CoreSettingsFunctor6createENS_7QNodeIdE
namespace Qt3DCore {
inline Qt3DCore::QBackendNode *CoreSettingsFunctor::create(Qt3DCore::QNodeId) const
{
    if (m_settings != nullptr) {
        qWarning() << "Core settings already exists";
        return nullptr;
    }

    m_settings = new CoreSettings;
    m_settings->setAspect(m_aspect);
    return m_settings;
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/aspect/coresettings.cpp, line 47, as _ZNK8Qt3DCore19CoreSettingsFunctor3getENS_7QNodeIdE
namespace Qt3DCore {
inline Qt3DCore::QBackendNode *CoreSettingsFunctor::get(Qt3DCore::QNodeId id) const
{
    Q_UNUSED(id);
    return m_settings;
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/aspect/coresettings.cpp, line 53, as _ZNK8Qt3DCore19CoreSettingsFunctor7destroyENS_7QNodeIdE
namespace Qt3DCore {
inline void CoreSettingsFunctor::destroy(Qt3DCore::QNodeId id) const
{
    Q_UNUSED(id);
    delete m_settings;
    m_settings = nullptr;
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  Qt3DCore::CoreSettingsFunctor::CoreSettingsFunctor(QCoreAspect *aspect)
extern "C" Q_DECL_EXPORT
Qt3DCore::CoreSettingsFunctor *ritual_ZN8Qt3DCore19CoreSettingsFunctorC1EPNS_11QCoreAspectE(
    Qt3DCore::QCoreAspect *aspect) {
  return new Qt3DCore::CoreSettingsFunctor(aspect);
}

//  Qt3DCore::QBackendNode
//      *Qt3DCore::CoreSettingsFunctor::create(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore19CoreSettingsFunctor6createENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DCore::CoreSettingsFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore19CoreSettingsFunctor3getENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DCore::CoreSettingsFunctor::destroy(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8Qt3DCore19CoreSettingsFunctor7destroyENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DCore::CoreSettingsFunctor::~CoreSettingsFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19CoreSettingsFunctorD1Ev(
    Qt3DCore::CoreSettingsFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DCore::CoreSettingsFunctor::create(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK8Qt3DCore19CoreSettingsFunctor6createENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::CoreSettingsFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DCore::CoreSettingsFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK8Qt3DCore19CoreSettingsFunctor3getENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::CoreSettingsFunctor::get(*id);
}

//  void Qt3DCore::CoreSettingsFunctor::destroy(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK8Qt3DCore19CoreSettingsFunctor7destroyENS_7QNodeIdE(
    const Qt3DCore::CoreSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DCore::CoreSettingsFunctor::destroy(*id);
}
