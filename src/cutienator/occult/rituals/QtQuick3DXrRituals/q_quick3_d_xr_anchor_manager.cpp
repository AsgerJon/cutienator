//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxranchormanager_visionos_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  'defined(Q_OS_VISIONOS)'. Qt builds the visionOS files of Quick3DXr
//  (its 'visionos' directory) only when VISIONOS is set, as its
//  CMakeLists.txt says, and installs the header named here for no other
//  system. Kept as it is when the generator runs again.
//  Completed by hand on 2026-11-25: the OpenXR version of the class,
//  which Qt builds when VISIONOS is not set, as the CMakeLists.txt of
//  Quick3DXr says, and when <openxr/openxr.h> is there. The file now
//  stands under either. Added: the thirteen wrappers of OpenXR calls
//  (enumerateSpaceSupportedComponents to requestSceneCapture); metaObject,
//  teardown, anchorCount and the destructor serve both versions, and
//  getCurrentSpaceId only the visionOS one. Left out of the OpenXR
//  version: what calls OpenXRHelpers::checkXrResult or
//  resolveXrFunction, which Qt does not export, the constructor, the
//  signals, and what takes or gives a QList or a QSet.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#if defined(Q_OS_VISIONOS) || __has_include(<openxr/openxr.h>)
#if defined(Q_OS_VISIONOS)
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranchormanager_visionos_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/QLoggingCategory>
#if defined(Q_OS_ANDROID)
# include <QtCore/private/qandroidextras_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#else
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranchormanager_openxr_p.h>
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qopenxrhelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif  // defined(Q_OS_VISIONOS), else OpenXR

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 132, as _ZN23QQuick3DXrAnchorManager8teardownEv
inline void QQuick3DXrAnchorManager::teardown()
{

}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 471, as _ZNK23QQuick3DXrAnchorManager11anchorCountEv
inline qsizetype QQuick3DXrAnchorManager::anchorCount() const
{
    return m_anchors.count();
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 56, as _ZN23QQuick3DXrAnchorManagerD1Ev
inline QQuick3DXrAnchorManager::~QQuick3DXrAnchorManager()
{

}

#if !defined(Q_OS_VISIONOS)
//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 588, as _ZN23QQuick3DXrAnchorManager33enumerateSpaceSupportedComponentsEP9XrSpace_TjPjP22XrSpaceComponentTypeFB
inline XrResult QQuick3DXrAnchorManager::enumerateSpaceSupportedComponents(XrSpace space, uint32_t componentTypeCapacityInput, uint32_t *componentTypeCountOutput, XrSpaceComponentTypeFB *componentTypes)
{
    return OpenXRHelpers::safeCall(xrEnumerateSpaceSupportedComponentsFB, space, componentTypeCapacityInput, componentTypeCountOutput, componentTypes);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 593, as _ZN23QQuick3DXrAnchorManager23getSpaceComponentStatusEP9XrSpace_T22XrSpaceComponentTypeFBP24XrSpaceComponentStatusFB
inline XrResult QQuick3DXrAnchorManager::getSpaceComponentStatus(XrSpace space, XrSpaceComponentTypeFB componentType, XrSpaceComponentStatusFB *status)
{
    return OpenXRHelpers::safeCall(xrGetSpaceComponentStatusFB, space, componentType, status);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 598, as _ZN23QQuick3DXrAnchorManager23setSpaceComponentStatusEP9XrSpace_TPK31XrSpaceComponentStatusSetInfoFBPm
inline XrResult QQuick3DXrAnchorManager::setSpaceComponentStatus(XrSpace space, const XrSpaceComponentStatusSetInfoFB *info, XrAsyncRequestIdFB *requestId)
{
    return OpenXRHelpers::safeCall(xrSetSpaceComponentStatusFB, space, info, requestId);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 603, as _ZN23QQuick3DXrAnchorManager12getSpaceUuidEP9XrSpace_TP6XrUuid
inline XrResult QQuick3DXrAnchorManager::getSpaceUuid(XrSpace space, XrUuidEXT *uuid)
{
    return OpenXRHelpers::safeCall(xrGetSpaceUuidFB, space, uuid);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 608, as _ZN23QQuick3DXrAnchorManager11querySpacesEPK28XrSpaceQueryInfoBaseHeaderFBPm
inline XrResult QQuick3DXrAnchorManager::querySpaces(const XrSpaceQueryInfoBaseHeaderFB *info, XrAsyncRequestIdFB *requestId)
{
    return OpenXRHelpers::safeCall(xrQuerySpacesFB, m_session, info, requestId);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 613, as _ZN23QQuick3DXrAnchorManager25retrieveSpaceQueryResultsEmP21XrSpaceQueryResultsFB
inline XrResult QQuick3DXrAnchorManager::retrieveSpaceQueryResults(XrAsyncRequestIdFB requestId, XrSpaceQueryResultsFB *results)
{
    return OpenXRHelpers::safeCall(xrRetrieveSpaceQueryResultsFB, m_session, requestId, results);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 618, as _ZN23QQuick3DXrAnchorManager21getSpaceBoundingBox2DEP9XrSpace_TP9XrRect2Df
inline XrResult QQuick3DXrAnchorManager::getSpaceBoundingBox2D(XrSpace space, XrRect2Df *boundingBox2DOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceBoundingBox2DFB, m_session, space, boundingBox2DOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 623, as _ZN23QQuick3DXrAnchorManager21getSpaceBoundingBox3DEP9XrSpace_TP11XrRect3DfFB
inline XrResult QQuick3DXrAnchorManager::getSpaceBoundingBox3D(XrSpace space, XrRect3DfFB *boundingBox3DOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceBoundingBox3DFB, m_session, space, boundingBox3DOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 628, as _ZN23QQuick3DXrAnchorManager22getSpaceSemanticLabelsEP9XrSpace_TP18XrSemanticLabelsFB
inline XrResult QQuick3DXrAnchorManager::getSpaceSemanticLabels(XrSpace space, XrSemanticLabelsFB *semanticLabelsOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceSemanticLabelsFB, m_session, space, semanticLabelsOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 633, as _ZN23QQuick3DXrAnchorManager18getSpaceBoundary2DEP9XrSpace_TP14XrBoundary2DFB
inline XrResult QQuick3DXrAnchorManager::getSpaceBoundary2D(XrSpace space, XrBoundary2DFB *boundary2DOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceBoundary2DFB, m_session, space, boundary2DOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 638, as _ZN23QQuick3DXrAnchorManager18getSpaceRoomLayoutEP9XrSpace_TP14XrRoomLayoutFB
inline XrResult QQuick3DXrAnchorManager::getSpaceRoomLayout(XrSpace space, XrRoomLayoutFB *roomLayoutOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceRoomLayoutFB, m_session, space, roomLayoutOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 643, as _ZN23QQuick3DXrAnchorManager17getSpaceContainerEP9XrSpace_TP18XrSpaceContainerFB
inline XrResult QQuick3DXrAnchorManager::getSpaceContainer(XrSpace space, XrSpaceContainerFB *spaceContainerOutput)
{
    return OpenXRHelpers::safeCall(xrGetSpaceContainerFB, m_session, space, spaceContainerOutput);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qquick3dxranchormanager_openxr.cpp, line 648, as _ZN23QQuick3DXrAnchorManager19requestSceneCaptureEPK27XrSceneCaptureRequestInfoFBPm
inline XrResult QQuick3DXrAnchorManager::requestSceneCapture(const XrSceneCaptureRequestInfoFB *info, XrAsyncRequestIdFB *requestId)
{
    return OpenXRHelpers::safeCall(xrRequestSceneCaptureFB, m_session, info, requestId);
}
#endif  // !defined(Q_OS_VISIONOS)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrAnchorManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DXrAnchorManager10metaObjectEv(
    const QQuick3DXrAnchorManager *self) {
  return self->metaObject();
}

//  void *QQuick3DXrAnchorManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DXrAnchorManager11qt_metacastEPKc(
    QQuick3DXrAnchorManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

#if defined(Q_OS_VISIONOS)
//  QtQuick3DXr::XrSpaceId QQuick3DXrAnchorManager::getCurrentSpaceId() const
extern "C" Q_DECL_EXPORT
QtQuick3DXr::XrSpaceId ritual_ZNK23QQuick3DXrAnchorManager17getCurrentSpaceIdEv(
    const QQuick3DXrAnchorManager *self) {
  return self->getCurrentSpaceId();
}
#endif  // defined(Q_OS_VISIONOS)

//  void QQuick3DXrAnchorManager::teardown()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManager8teardownEv(
    QQuick3DXrAnchorManager *self) {
  self->teardown();
}

//  qsizetype QQuick3DXrAnchorManager::anchorCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QQuick3DXrAnchorManager11anchorCountEv(
    const QQuick3DXrAnchorManager *self) {
  return self->anchorCount();
}

//  QQuick3DXrAnchorManager::~QQuick3DXrAnchorManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrAnchorManagerD1Ev(QQuick3DXrAnchorManager *self) {
  delete self;
}

#if !defined(Q_OS_VISIONOS)
//  XrResult
//      QQuick3DXrAnchorManager::enumerateSpaceSupportedComponents(XrSpace
//      space, uint32_t componentTypeCapacityInput, uint32_t
//      *componentTypeCountOutput, XrSpaceComponentTypeFB *componentTypes)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager33enumerateSpaceSupportedComponentsEP9XrSpace_TjPjP22XrSpaceComponentTypeFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    uint32_t componentTypeCapacityInput,
    uint32_t *componentTypeCountOutput,
    XrSpaceComponentTypeFB *componentTypes) {
  return self->enumerateSpaceSupportedComponents(space, componentTypeCapacityInput, componentTypeCountOutput, componentTypes);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceComponentStatus(XrSpace space,
//      XrSpaceComponentTypeFB componentType, XrSpaceComponentStatusFB
//      *status)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager23getSpaceComponentStatusEP9XrSpace_T22XrSpaceComponentTypeFBP24XrSpaceComponentStatusFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrSpaceComponentTypeFB componentType,
    XrSpaceComponentStatusFB *status) {
  return self->getSpaceComponentStatus(space, componentType, status);
}

//  XrResult QQuick3DXrAnchorManager::setSpaceComponentStatus(XrSpace space,
//      const XrSpaceComponentStatusSetInfoFB *info, XrAsyncRequestIdFB
//      *requestId)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager23setSpaceComponentStatusEP9XrSpace_TPK31XrSpaceComponentStatusSetInfoFBPm(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    const XrSpaceComponentStatusSetInfoFB *info,
    XrAsyncRequestIdFB *requestId) {
  return self->setSpaceComponentStatus(space, info, requestId);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceUuid(XrSpace space, XrUuidEXT
//      *uuid)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager12getSpaceUuidEP9XrSpace_TP6XrUuid(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrUuidEXT *uuid) {
  return self->getSpaceUuid(space, uuid);
}

//  XrResult QQuick3DXrAnchorManager::querySpaces(const
//      XrSpaceQueryInfoBaseHeaderFB *info, XrAsyncRequestIdFB *requestId)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager11querySpacesEPK28XrSpaceQueryInfoBaseHeaderFBPm(
    QQuick3DXrAnchorManager *self,
    const XrSpaceQueryInfoBaseHeaderFB *info,
    XrAsyncRequestIdFB *requestId) {
  return self->querySpaces(info, requestId);
}

//  XrResult
//      QQuick3DXrAnchorManager::retrieveSpaceQueryResults(XrAsyncRequestIdFB
//      requestId, XrSpaceQueryResultsFB *results)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager25retrieveSpaceQueryResultsEmP21XrSpaceQueryResultsFB(
    QQuick3DXrAnchorManager *self,
    XrAsyncRequestIdFB requestId,
    XrSpaceQueryResultsFB *results) {
  return self->retrieveSpaceQueryResults(requestId, results);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceBoundingBox2D(XrSpace space,
//      XrRect2Df *boundingBox2DOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager21getSpaceBoundingBox2DEP9XrSpace_TP9XrRect2Df(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrRect2Df *boundingBox2DOutput) {
  return self->getSpaceBoundingBox2D(space, boundingBox2DOutput);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceBoundingBox3D(XrSpace space,
//      XrRect3DfFB *boundingBox3DOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager21getSpaceBoundingBox3DEP9XrSpace_TP11XrRect3DfFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrRect3DfFB *boundingBox3DOutput) {
  return self->getSpaceBoundingBox3D(space, boundingBox3DOutput);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceSemanticLabels(XrSpace space,
//      XrSemanticLabelsFB *semanticLabelsOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager22getSpaceSemanticLabelsEP9XrSpace_TP18XrSemanticLabelsFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrSemanticLabelsFB *semanticLabelsOutput) {
  return self->getSpaceSemanticLabels(space, semanticLabelsOutput);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceBoundary2D(XrSpace space,
//      XrBoundary2DFB *boundary2DOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager18getSpaceBoundary2DEP9XrSpace_TP14XrBoundary2DFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrBoundary2DFB *boundary2DOutput) {
  return self->getSpaceBoundary2D(space, boundary2DOutput);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceRoomLayout(XrSpace space,
//      XrRoomLayoutFB *roomLayoutOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager18getSpaceRoomLayoutEP9XrSpace_TP14XrRoomLayoutFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrRoomLayoutFB *roomLayoutOutput) {
  return self->getSpaceRoomLayout(space, roomLayoutOutput);
}

//  XrResult QQuick3DXrAnchorManager::getSpaceContainer(XrSpace space,
//      XrSpaceContainerFB *spaceContainerOutput)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager17getSpaceContainerEP9XrSpace_TP18XrSpaceContainerFB(
    QQuick3DXrAnchorManager *self,
    XrSpace space,
    XrSpaceContainerFB *spaceContainerOutput) {
  return self->getSpaceContainer(space, spaceContainerOutput);
}

//  XrResult QQuick3DXrAnchorManager::requestSceneCapture(const
//      XrSceneCaptureRequestInfoFB *info, XrAsyncRequestIdFB *requestId)
extern "C" Q_DECL_EXPORT
XrResult ritual_ZN23QQuick3DXrAnchorManager19requestSceneCaptureEPK27XrSceneCaptureRequestInfoFBPm(
    QQuick3DXrAnchorManager *self,
    const XrSceneCaptureRequestInfoFB *info,
    XrAsyncRequestIdFB *requestId) {
  return self->requestSceneCapture(info, requestId);
}
#endif  // !defined(Q_OS_VISIONOS)

#endif  // defined(Q_OS_VISIONOS) || OpenXR
