//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qvkconvenience_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qvkconvenience_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

#if QT_CONFIG(opengl)
//  VkFormat QVkConvenience::vkFormatFromGlFormat(uint glFormat)
extern "C" Q_DECL_EXPORT
VkFormat *ritual_ZN14QVkConvenience20vkFormatFromGlFormatEj(uint glFormat) {
  return new VkFormat(QVkConvenience::vkFormatFromGlFormat(glFormat));
}
#endif  // QT_CONFIG(opengl)

//  QVkConvenience::~QVkConvenience()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QVkConvenienceD1Ev(QVkConvenience *self) {
  delete self;
}

//  a VkFormat a ritual of QVkConvenience gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVkConvenience__VkFormat(VkFormat *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan)
