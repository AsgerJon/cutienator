//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGColorAttachment::QSSGColorAttachment(const QByteArray &name)
extern "C" Q_DECL_EXPORT
QSSGColorAttachment *ritual_ZN19QSSGColorAttachmentC1ERK10QByteArray(
    const QByteArray *name) {
  return new QSSGColorAttachment(*name);
}

//  QSSGRenderTextureFormat QSSGColorAttachment::format() const
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat *ritual_ZNK19QSSGColorAttachment6formatEv(
    const QSSGColorAttachment *self) {
  return new QSSGRenderTextureFormat(self->format());
}

//  QSSGColorAttachment::QSSGColorAttachment(const QByteArray &name,
//      CommandType type)
extern "C" Q_DECL_EXPORT
QSSGColorAttachment *ritual_ZN19QSSGColorAttachmentC1ERK10QByteArray11CommandType(
    const QByteArray *name,
    CommandType type) {
  return new QSSGColorAttachment(*name, type);
}

//  QSSGColorAttachment::~QSSGColorAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGColorAttachmentD1Ev(QSSGColorAttachment *self) {
  delete self;
}
