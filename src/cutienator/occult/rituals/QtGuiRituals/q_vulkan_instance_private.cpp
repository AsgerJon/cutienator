//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qvulkaninstance_p.h, Qt 6.12.0, as the Qt
//  of Windows installs it. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qvulkaninstance_p.h>
#include <QtGui/6.12.0/QtGui/qpa/qplatformvulkaninstance.h>

//  QVulkanInstancePrivate::QVulkanInstancePrivate(QVulkanInstance *q)
extern "C" Q_DECL_EXPORT
QVulkanInstancePrivate *ritual_ZN22QVulkanInstancePrivateC1EP15QVulkanInstance(
    QVulkanInstance *q) {
  return new QVulkanInstancePrivate(q);
}

//  QVulkanInstancePrivate::~QVulkanInstancePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVulkanInstancePrivateD1Ev(QVulkanInstancePrivate *self) {
  delete self;
}

//  QVulkanInstancePrivate *QVulkanInstancePrivate::get(QVulkanInstance *q)
extern "C" Q_DECL_EXPORT
QVulkanInstancePrivate *ritual_ZN22QVulkanInstancePrivate3getEP15QVulkanInstance(
    QVulkanInstance *q) {
  return QVulkanInstancePrivate::get(q);
}

//  bool QVulkanInstancePrivate::ensureVulkan()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QVulkanInstancePrivate12ensureVulkanEv(
    QVulkanInstancePrivate *self) {
  return self->ensureVulkan();
}

//  void QVulkanInstancePrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVulkanInstancePrivate5resetEv(
    QVulkanInstancePrivate *self) {
  self->reset();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
