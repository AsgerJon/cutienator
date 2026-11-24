//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qvulkandefaultinstance_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qvulkandefaultinstance_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Flags QVulkanDefaultInstance::flags()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QVulkanDefaultInstance5flagsEv() {
  return static_cast<int>(QVulkanDefaultInstance::flags().toInt());
}

//  void QVulkanDefaultInstance::setFlag(Flag flag, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVulkanDefaultInstance7setFlagENS_4FlagEb(
    QVulkanDefaultInstance::Flag flag,
    bool on) {
  QVulkanDefaultInstance::setFlag(flag, on);
}

//  bool QVulkanDefaultInstance::hasInstance()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QVulkanDefaultInstance11hasInstanceEv() {
  return QVulkanDefaultInstance::hasInstance();
}

//  void QVulkanDefaultInstance::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVulkanDefaultInstance7cleanupEv() {
  QVulkanDefaultInstance::cleanup();
}

//  QVulkanDefaultInstance::~QVulkanDefaultInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVulkanDefaultInstanceD1Ev(QVulkanDefaultInstance *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan)
