//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturehelper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/qopenglpixeltransferoptions.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qopengltexturehelper_p.h"
#include <QOpenGLContext>
#include <private/qopenglextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopengltexturehelper.cpp, line 297, as _ZN20QOpenGLTextureHelper18dsa_TextureImage1DEjjjijiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage1DEXT(texture, target, level, internalFormat, width, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 291, as _ZN20QOpenGLTextureHelper18dsa_TextureImage2DEjjjijiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DEXT(texture, target, level, internalFormat, width, height, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 285, as _ZN20QOpenGLTextureHelper18dsa_TextureImage3DEjjjijiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DEXT(texture, target, level, internalFormat, width, height, depth, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 315, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage1DEjjjiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage1DEXT(texture, target, level, xoffset, width, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 309, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage2DEjjjiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 303, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage3DEjjjiiiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 243, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterfvEjjjjPKf
inline void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfvEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 231, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterivEjjjjPKi
inline void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterivEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 351, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage1DEjjjijiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage1DEXT(texture, target, level, internalFormat, width, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 357, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage2DEjjjijiiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage2DEXT(texture, target, level, internalFormat, width, height, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 363, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage3DEjjjijiiiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage3DEXT(texture, target, level, internalFormat, width, height, depth, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 333, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage1DEjjjiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage1DEXT(texture, target, level, xoffset, width, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 339, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage2DEjjjiiiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 345, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage3DEjjjiiiiiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 225, as _ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji
inline void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint param)
{
    Q_UNUSED(bindingTarget);
    TextureParameteriEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 237, as _ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf
inline void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat param)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 249, as _ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj
inline void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture, GLenum target, GLenum bindingTarget)
{
    Q_UNUSED(bindingTarget);
    GenerateTextureMipmapEXT(texture, target);
}

//  from src/opengl/qopengltexturehelper.cpp, line 255, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii
inline void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DEXT(texture, target, levels, internalFormat, width, height, depth);
}

//  from src/opengl/qopengltexturehelper.cpp, line 261, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii
inline void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DEXT(texture, target, levels, internalFormat, width, height);
}

//  from src/opengl/qopengltexturehelper.cpp, line 267, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji
inline void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width)
{
    Q_UNUSED(bindingTarget);
    TextureStorage1DEXT(texture, target, levels, internalFormat, width);
}

//  from src/opengl/qopengltexturehelper.cpp, line 273, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEjjjijiiih
inline void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DMultisampleEXT(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 279, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEjjjijiih
inline void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DMultisampleEXT(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 321, as _ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjjiiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DMultisampleNV(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 327, as _ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjjiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DMultisampleNV(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}
//  -----------------------------------------------------------------------

//  void QOpenGLTextureHelper::glTextureParameteri(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureParameteriEjjjji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLint param) {
  self->glTextureParameteri(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::glTextureParameterf(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureParameterfEjjjjf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLfloat param) {
  self->glTextureParameterf(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::glGenerateTextureMipmap(GLuint texture, GLenum
//      target, GLenum bindingTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glGenerateTextureMipmapEjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget) {
  self->glGenerateTextureMipmap(texture, target, bindingTarget);
}

//  void QOpenGLTextureHelper::glTextureStorage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage3DEjjjijiii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTextureStorage3D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height,
      depth);
}

//  void QOpenGLTextureHelper::glTextureStorage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage2DEjjjijii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->glTextureStorage2D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height);
}

//  void QOpenGLTextureHelper::glTextureStorage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage1DEjjjiji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->glTextureStorage1D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width);
}

//  void QOpenGLTextureHelper::glTextureStorage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glTextureStorage3DMultisampleEjjjijiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTextureStorage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureStorage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glTextureStorage2DMultisampleEjjjijiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTextureStorage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureImage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper27glTextureImage3DMultisampleEjjjiiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTextureImage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureImage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper27glTextureImage2DMultisampleEjjjiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTextureImage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLint param) {
  self->dsa_TextureParameteri(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLfloat param) {
  self->dsa_TextureParameterf(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture,
//      GLenum target, GLenum bindingTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget) {
  self->dsa_GenerateTextureMipmap(texture, target, bindingTarget);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->dsa_TextureStorage3D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height,
      depth);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->dsa_TextureStorage2D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->dsa_TextureStorage1D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEjjjijiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureStorage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEjjjijiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureStorage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjjiiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureImage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjjiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureImage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper15glActiveTextureEj(
    QOpenGLTextureHelper *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLTextureHelper::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glGenerateMipmapEj(
    QOpenGLTextureHelper *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLTextureHelper::glTexImage3DMultisample(GLenum target, GLsizei
//      samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei
//      depth, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glTexImage3DMultisampleEjiiiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTexImage3DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexImage2DMultisample(GLenum target, GLsizei
//      samples, GLint internalFormat, GLsizei width, GLsizei height,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glTexImage2DMultisampleEjiiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTexImage2DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexStorage3D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage3DEjijiii(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTexStorage3D(target, levels, internalFormat, width, height, depth);
}

//  void QOpenGLTextureHelper::glTexStorage2D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage2DEjijii(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->glTexStorage2D(target, levels, internalFormat, width, height);
}

//  void QOpenGLTextureHelper::glTexStorage1D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage1DEjiji(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->glTexStorage1D(target, levels, internalFormat, width);
}

//  void QOpenGLTextureHelper::glTexStorage3DMultisample(GLenum target,
//      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glTexStorage3DMultisampleEjijiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTexStorage3DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexStorage2DMultisample(GLenum target,
//      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
//      height, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glTexStorage2DMultisampleEjijiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTexStorage2DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureView(GLuint texture, GLenum target,
//      GLuint origTexture, GLenum internalFormat, GLuint minLevel, GLuint
//      numLevels, GLuint minLayer, GLuint numLayers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper13glTextureViewEjjjjjjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLuint origTexture,
    GLenum internalFormat,
    GLuint minLevel,
    GLuint numLevels,
    GLuint minLayer,
    GLuint numLayers) {
  self->glTextureView(
      texture,
      target,
      origTexture,
      internalFormat,
      minLevel,
      numLevels,
      minLayer,
      numLayers);
}

//  QOpenGLPixelTransferOptions
//      QOpenGLTextureHelper::savePixelUploadOptions()
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN20QOpenGLTextureHelper22savePixelUploadOptionsEv(
    QOpenGLTextureHelper *self) {
  return new QOpenGLPixelTransferOptions(self->savePixelUploadOptions());
}

//  void QOpenGLTextureHelper::setPixelUploadOptions(const
//      QOpenGLPixelTransferOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21setPixelUploadOptionsERK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    const QOpenGLPixelTransferOptions *options) {
  self->setPixelUploadOptions(*options);
}

//  QOpenGLTextureHelper::~QOpenGLTextureHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelperD1Ev(QOpenGLTextureHelper *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
