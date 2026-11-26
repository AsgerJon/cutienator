//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the OpenGL headers of macOS lack the
//  twelve GL_*_KHR constants the code taken from Qt for
//  'updateCompositionMode' uses, so the file defines them where they
//  are missing, as Qt's 'qopenglpaintengine.cpp' does for itself, with
//  Qt's own '#ifndef' lines and values. Kept as it is when the
//  generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopenglgradientcache_p.h>
#include <QtOpenGL/private/qopengltexturecache_p.h>
#include <QtOpenGL/private/qopenglpaintengine_p.h>
#include <QtOpenGL/private/qopenglpaintdevice_p.h>
#include <string.h> //for memcpy
#include <QtCore/qmath.h>
#include <QtGui/private/qopengl_p.h>
#include <QtGui/private/qopenglcontext_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qpaintengineex_p.h>
#include <QtGui/QPaintEngine>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qdatabuffer_p.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtOpenGL/private/qopenglengineshadermanager_p.h>
#include <QtOpenGL/private/qopengl2pexvertexarray_p.h>
#include <QtOpenGL/private/qopengltextureglyphcache_p.h>
#include <QtCore/QDebug>
#include <QtOpenGL/private/qopengl2pexvertexarray_p.h>
#include <QtGui/private/qbezier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  The constants Qt defines for itself where the OpenGL headers
//  lack them.
//  from src/opengl/qopenglpaintengine.cpp, line 57
#ifndef GL_KHR_blend_equation_advanced
#define GL_KHR_blend_equation_advanced 1
#define GL_MULTIPLY_KHR                   0x9294
#define GL_SCREEN_KHR                     0x9295
#define GL_OVERLAY_KHR                    0x9296
#define GL_DARKEN_KHR                     0x9297
#define GL_LIGHTEN_KHR                    0x9298
#define GL_COLORDODGE_KHR                 0x9299
#define GL_COLORBURN_KHR                  0x929A
#define GL_HARDLIGHT_KHR                  0x929B
#define GL_SOFTLIGHT_KHR                  0x929C
#define GL_DIFFERENCE_KHR                 0x929E
#define GL_EXCLUSION_KHR                  0x92A0
#endif /* GL_KHR_blend_equation_advanced */
//  from src/opengl/qopenglpaintengine.cpp, line 72
#ifndef GL_KHR_blend_equation_advanced_coherent
#define GL_KHR_blend_equation_advanced_coherent 1
#define GL_BLEND_ADVANCED_COHERENT_KHR    0x9285
#endif /* GL_KHR_blend_equation_advanced_coherent */

//  from src/opengl/qopenglpaintengine.cpp, line 2439, as _ZN28QOpenGL2PaintEngineExPrivate9writeClipERK11QVectorPathj
inline void QOpenGL2PaintEngineExPrivate::writeClip(const QVectorPath &path, uint value)
{
    transferMode(BrushDrawingMode);

    if (snapToPixelGrid) {
        snapToPixelGrid = false;
        matrixDirty = true;
    }

    if (matrixDirty)
        updateMatrix();

    stencilClean = false;

    const bool singlePass = !path.hasWindingFill()
        && (((q->state()->currentClip == maxClip - 1) && q->state()->clipTestEnabled)
            || q->state()->needsClipBufferClear);
    const uint referenceClipValue = q->state()->needsClipBufferClear ? 1 : q->state()->currentClip;

    if (q->state()->needsClipBufferClear)
        clearClip(1);

    if (path.isEmpty()) {
        funcs.glEnable(GL_STENCIL_TEST);
        funcs.glStencilFunc(GL_LEQUAL, value, ~GL_STENCIL_HIGH_BIT);
        return;
    }

    if (q->state()->clipTestEnabled)
        funcs.glStencilFunc(GL_LEQUAL, q->state()->currentClip, ~GL_STENCIL_HIGH_BIT);
    else
        funcs.glStencilFunc(GL_ALWAYS, 0, 0xff);

    vertexCoordinateArray.clear();
    vertexCoordinateArray.addPath(path, inverseScale, false);

    if (!singlePass)
        fillStencilWithVertexArray(vertexCoordinateArray, path.hasWindingFill());

    funcs.glColorMask(false, false, false, false);
    funcs.glEnable(GL_STENCIL_TEST);
    useSimpleShader();

    if (singlePass) {
        // Under these conditions we can set the new stencil value in a single
        // pass, by using the current value and the "new value" as the toggles

        funcs.glStencilFunc(GL_LEQUAL, referenceClipValue, ~GL_STENCIL_HIGH_BIT);
        funcs.glStencilOp(GL_KEEP, GL_INVERT, GL_INVERT);
        funcs.glStencilMask(value ^ referenceClipValue);

        drawVertexArrays(vertexCoordinateArray, GL_TRIANGLE_FAN);
    } else {
        funcs.glStencilOp(GL_KEEP, GL_REPLACE, GL_REPLACE);
        funcs.glStencilMask(0xff);

        if (!q->state()->clipTestEnabled && path.hasWindingFill()) {
            // Pass when any clip bit is set, set high bit
            funcs.glStencilFunc(GL_NOTEQUAL, GL_STENCIL_HIGH_BIT, ~GL_STENCIL_HIGH_BIT);
            composite(vertexCoordinateArray.boundingRect());
        }

        // Pass when high bit is set, replace stencil value with new clip value
        funcs.glStencilFunc(GL_NOTEQUAL, value, GL_STENCIL_HIGH_BIT);

        composite(vertexCoordinateArray.boundingRect());
    }

    funcs.glStencilFunc(GL_LEQUAL, value, ~GL_STENCIL_HIGH_BIT);
    funcs.glStencilMask(0);

    funcs.glColorMask(true, true, true, true);
}

//  from src/opengl/qopengl2pexvertexarray.cpp, line 11, as _ZN22QOpenGL2PEXVertexArray5clearEv
inline void QOpenGL2PEXVertexArray::clear()
{
    vertexArray.reset();
    vertexArrayStops.reset();
    boundingRectDirty = true;
}

//  from src/opengl/qopengl2pexvertexarray.cpp, line 51, as _ZN22QOpenGL2PEXVertexArray7addPathERK11QVectorPathfb
inline void QOpenGL2PEXVertexArray::addPath(const QVectorPath &path, GLfloat curveInverseScale, bool outline)
{
    const QPointF* const points = reinterpret_cast<const QPointF*>(path.points());
    const QPainterPath::ElementType* const elements = path.elements();

    if (boundingRectDirty) {
        minX = maxX = points[0].x();
        minY = maxY = points[0].y();
        boundingRectDirty = false;
    }

    if (!outline && !path.isConvex())
        addCentroid(path, 0);

    int lastMoveTo = vertexArray.size();
    vertexArray.add(points[0]); // The first element is always a moveTo

    do {
        if (!elements) {
//             qDebug("QVectorPath has no elements");
            // If the path has a null elements pointer, the elements implicitly
            // start with a moveTo (already added) and continue with lineTos:
            for (int i=1; i<path.elementCount(); ++i)
                lineToArray(points[i].x(), points[i].y());

            break;
        }
//         qDebug("QVectorPath has element types");

        for (int i=1; i<path.elementCount(); ++i) {
            switch (elements[i]) {
            case QPainterPath::MoveToElement:
                if (!outline)
                    addClosingLine(lastMoveTo);
//                qDebug("element[%d] is a MoveToElement", i);
                vertexArrayStops.add(vertexArray.size());
                if (!outline) {
                    if (!path.isConvex()) addCentroid(path, i);
                    lastMoveTo = vertexArray.size();
                }
                lineToArray(points[i].x(), points[i].y()); // Add the moveTo as a new vertex
                break;
            case QPainterPath::LineToElement:
//                qDebug("element[%d] is a LineToElement", i);
                lineToArray(points[i].x(), points[i].y());
                break;
            case QPainterPath::CurveToElement: {
                QBezier b = QBezier::fromPoints(*(((const QPointF *) points) + i - 1),
                                                points[i],
                                                points[i+1],
                                                points[i+2]);
                QRectF bounds = b.bounds();
                // threshold based on same algorithm as in qtriangulatingstroker.cpp
                int threshold = qMin<float>(64, qMax(bounds.width(), bounds.height()) * 3.14f / (curveInverseScale * 6));
                if (threshold < 3) threshold = 3;
                qreal one_over_threshold_minus_1 = qreal(1) / (threshold - 1);
                for (int t=0; t<threshold; ++t) {
                    QPointF pt = b.pointAt(t * one_over_threshold_minus_1);
                    lineToArray(pt.x(), pt.y());
                }
                i += 2;
                break; }
            default:
                break;
            }
        }
    } while (0);

    if (!outline)
        addClosingLine(lastMoveTo);
    vertexArrayStops.add(vertexArray.size());
}

//  from src/opengl/qopenglpaintengine.cpp, line 1315, as _ZN28QOpenGL2PaintEngineExPrivate16drawVertexArraysEPKfPiij
inline void QOpenGL2PaintEngineExPrivate::drawVertexArrays(const float *data, int *stops, int stopCount,
                                                GLenum primitive)
{
    // Now setup the pointer to the vertex array:
    uploadData(QT_VERTEX_COORDS_ATTR, data, stops[stopCount-1] * 2);

    int previousStop = 0;
    for (int i=0; i<stopCount; ++i) {
        int stop = stops[i];

        funcs.glDrawArrays(primitive, previousStop, stop - previousStop);
        previousStop = stop;
    }
}

//  from src/opengl/qopenglpaintengine.cpp, line 1090, as _ZN28QOpenGL2PaintEngineExPrivate26fillStencilWithVertexArrayEPKfiPiiRK11QOpenGLRectNS_15StencilFillModeE
inline void QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(const float *data,
                                                          int count,
                                                          int *stops,
                                                          int stopCount,
                                                          const QOpenGLRect &bounds,
                                                          StencilFillMode mode)
{
    Q_ASSERT(count || stops);

//     qDebug("QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray()");
    funcs.glStencilMask(0xff); // Enable stencil writes

    if (dirtyStencilRegion.intersects(currentScissorBounds)) {
        const QRegion clearRegion = dirtyStencilRegion.intersected(currentScissorBounds);
        funcs.glClearStencil(0); // Clear to zero
        for (const QRect &rect : clearRegion) {
#ifndef QT_GL_NO_SCISSOR_TEST
            setScissor(rect);
#endif
            funcs.glClear(GL_STENCIL_BUFFER_BIT);
        }

        dirtyStencilRegion -= currentScissorBounds;

#ifndef QT_GL_NO_SCISSOR_TEST
        updateClipScissorTest();
#endif
    }

    funcs.glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE); // Disable color writes
    useSimpleShader();
#ifndef QT_NO_DEBUG
    if (ctx->format().stencilBufferSize() <= 0)
        qWarning("OpenGL paint engine: attempted to use stencil test without requesting a stencil buffer.");
#endif
    funcs.glEnable(GL_STENCIL_TEST); // For some reason, this has to happen _after_ the simple shader is use()'d

    if (mode == WindingFillMode) {
        Q_ASSERT(stops && !count);
        if (q->state()->clipTestEnabled) {
            // Flatten clip values higher than current clip, and set high bit to match current clip
            funcs.glStencilFunc(GL_LEQUAL, GL_STENCIL_HIGH_BIT | q->state()->currentClip, ~GL_STENCIL_HIGH_BIT);
            funcs.glStencilOp(GL_KEEP, GL_REPLACE, GL_REPLACE);
            composite(bounds);

            funcs.glStencilFunc(GL_EQUAL, GL_STENCIL_HIGH_BIT, GL_STENCIL_HIGH_BIT);
        } else if (!stencilClean) {
            // Clear stencil buffer within bounding rect
            funcs.glStencilFunc(GL_ALWAYS, 0, 0xff);
            funcs.glStencilOp(GL_ZERO, GL_ZERO, GL_ZERO);
            composite(bounds);
        }

        // Inc. for front-facing triangle
        funcs.glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_INCR_WRAP, GL_INCR_WRAP);
        // Dec. for back-facing "holes"
        funcs.glStencilOpSeparate(GL_BACK, GL_KEEP, GL_DECR_WRAP, GL_DECR_WRAP);
        funcs.glStencilMask(~GL_STENCIL_HIGH_BIT);
        drawVertexArrays(data, stops, stopCount, GL_TRIANGLE_FAN);

        if (q->state()->clipTestEnabled) {
            // Clear high bit of stencil outside of path
            funcs.glStencilFunc(GL_EQUAL, q->state()->currentClip, ~GL_STENCIL_HIGH_BIT);
            funcs.glStencilOp(GL_KEEP, GL_REPLACE, GL_REPLACE);
            funcs.glStencilMask(GL_STENCIL_HIGH_BIT);
            composite(bounds);
        }
    } else if (mode == OddEvenFillMode) {
        funcs.glStencilMask(GL_STENCIL_HIGH_BIT);
        funcs.glStencilOp(GL_KEEP, GL_KEEP, GL_INVERT); // Simply invert the stencil bit
        drawVertexArrays(data, stops, stopCount, GL_TRIANGLE_FAN);

    } else { // TriStripStrokeFillMode
        Q_ASSERT(count && !stops); // tristrips generated directly, so no vertexArray or stops
        funcs.glStencilMask(GL_STENCIL_HIGH_BIT);
#if 0
        funcs.glStencilOp(GL_KEEP, GL_KEEP, GL_INVERT); // Simply invert the stencil bit
        setVertexAttributePointer(QT_VERTEX_COORDS_ATTR, data);
        funcs.glDrawArrays(GL_TRIANGLE_STRIP, 0, count);
#else

        funcs.glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);
        if (q->state()->clipTestEnabled) {
            funcs.glStencilFunc(GL_LEQUAL, q->state()->currentClip | GL_STENCIL_HIGH_BIT,
                                ~GL_STENCIL_HIGH_BIT);
        } else {
            funcs.glStencilFunc(GL_ALWAYS, GL_STENCIL_HIGH_BIT, 0xff);
        }

        uploadData(QT_VERTEX_COORDS_ATTR, data, count * 2);
        funcs.glDrawArrays(GL_TRIANGLE_STRIP, 0, count);
#endif
    }

    // Enable color writes & disable stencil writes
    funcs.glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);
}

//  from src/opengl/qopenglpaintengine.cpp, line 84, as _ZN28QOpenGL2PaintEngineExPrivateD1Ev
inline QOpenGL2PaintEngineExPrivate::~QOpenGL2PaintEngineExPrivate()
{
    delete shaderManager;

    vertexBuffer.destroy();
    texCoordBuffer.destroy();
    opacityBuffer.destroy();
    indexBuffer.destroy();
    vao.destroy();

    if (elementIndicesVBOId != 0) {
        funcs.glDeleteBuffers(1, &elementIndicesVBOId);
        elementIndicesVBOId = 0;
    }
}

//  from src/opengl/qopenglpaintengine.cpp, line 444, as _ZN28QOpenGL2PaintEngineExPrivate12updateMatrixEv
inline void QOpenGL2PaintEngineExPrivate::updateMatrix()
{
//     qDebug("QOpenGL2PaintEngineExPrivate::updateMatrix()");

    const QTransform& transform = q->state()->matrix;

    // The projection matrix converts from Qt's coordinate system to GL's coordinate system
    //    * GL's viewport is 2x2, Qt's is width x height
    //    * GL has +y -> -y going from bottom -> top, Qt is the other way round
    //    * GL has [0,0] in the center, Qt has it in the top-left
    //
    // This results in the Projection matrix below, which is multiplied by the painter's
    // transformation matrix, as shown below:
    //
    //                Projection Matrix                      Painter Transform
    // ------------------------------------------------   ------------------------
    // | 2.0 / width  |      0.0      |     -1.0      |   |  m11  |  m21  |  dx  |
    // |     0.0      | -2.0 / height |      1.0      | * |  m12  |  m22  |  dy  |
    // |     0.0      |      0.0      |      1.0      |   |  m13  |  m23  |  m33 |
    // ------------------------------------------------   ------------------------
    //
    // NOTE: The resultant matrix is also transposed, as GL expects column-major matracies

    const GLfloat wfactor = 2.0f / width;
    GLfloat hfactor = -2.0f / height;

    GLfloat dx = transform.dx();
    GLfloat dy = transform.dy();

    if (device->paintFlipped()) {
        hfactor *= -1;
        dy -= height;
    }

    // Non-integer translates can have strange effects for some rendering operations such as
    // anti-aliased text rendering. In such cases, we snap the translate to the pixel grid.
    if (snapToPixelGrid && transform.type() == QTransform::TxTranslate) {
        // 0.50 needs to rounded down to 0.0 for consistency with raster engine:
        dx = std::ceil(dx - 0.5f);
        dy = std::ceil(dy - 0.5f);
    }
    pmvMatrix[0][0] = (wfactor * transform.m11())  - transform.m13();
    pmvMatrix[1][0] = (wfactor * transform.m21())  - transform.m23();
    pmvMatrix[2][0] = (wfactor * dx) - transform.m33();
    pmvMatrix[0][1] = (hfactor * transform.m12())  + transform.m13();
    pmvMatrix[1][1] = (hfactor * transform.m22())  + transform.m23();
    pmvMatrix[2][1] = (hfactor * dy) + transform.m33();
    pmvMatrix[0][2] = transform.m13();
    pmvMatrix[1][2] = transform.m23();
    pmvMatrix[2][2] = transform.m33();

    // 1/10000 == 0.0001, so we have good enough res to cover curves
    // that span the entire widget...
    inverseScale = qMax(1 / qMax( qMax(qAbs(transform.m11()), qAbs(transform.m22())),
                                  qMax(qAbs(transform.m12()), qAbs(transform.m21())) ),
                        qreal(0.0001));

    matrixDirty = false;
    matrixUniformDirty = true;

    // Set the PMV matrix attribute. As we use an attributes rather than uniforms, we only
    // need to do this once for every matrix change and persists across all shader programs.
    funcs.glVertexAttrib3fv(QT_PMV_MATRIX_1_ATTR, pmvMatrix[0]);
    funcs.glVertexAttrib3fv(QT_PMV_MATRIX_2_ATTR, pmvMatrix[1]);
    funcs.glVertexAttrib3fv(QT_PMV_MATRIX_3_ATTR, pmvMatrix[2]);

    dasher.setInvScale(inverseScale);
    stroker.setInvScale(inverseScale);
}

//  from src/opengl/qopenglpaintengine.cpp, line 515, as _ZN28QOpenGL2PaintEngineExPrivate21updateCompositionModeEv
inline void QOpenGL2PaintEngineExPrivate::updateCompositionMode()
{
    // NOTE: The entire paint engine works on pre-multiplied data - which is why some of these
    //       composition modes look odd.
//     qDebug() << "QOpenGL2PaintEngineExPrivate::updateCompositionMode() - Setting GL composition mode for " << q->state()->composition_mode;
    if (ctx->functions()->hasOpenGLFeature(QOpenGLFunctions::BlendEquationAdvanced)) {
       if (q->state()->composition_mode <= QPainter::CompositionMode_Plus) {
           funcs.glDisable(GL_BLEND_ADVANCED_COHERENT_KHR);
           funcs.glBlendEquation(GL_FUNC_ADD);
       } else {
           funcs.glEnable(GL_BLEND_ADVANCED_COHERENT_KHR);
       }
       shaderManager->setCompositionMode(q->state()->composition_mode);
    } else {
        if (q->state()->composition_mode > QPainter::CompositionMode_Plus) {
            qWarning("Unsupported composition mode");
            compositionModeDirty = false;
            return;
        }
    }
    switch(q->state()->composition_mode) {
    case QPainter::CompositionMode_SourceOver:
        funcs.glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_DestinationOver:
        funcs.glBlendFunc(GL_ONE_MINUS_DST_ALPHA, GL_ONE);
        break;
    case QPainter::CompositionMode_Clear:
        funcs.glBlendFunc(GL_ZERO, GL_ZERO);
        break;
    case QPainter::CompositionMode_Source:
        funcs.glBlendFunc(GL_ONE, GL_ZERO);
        break;
    case QPainter::CompositionMode_Destination:
        funcs.glBlendFunc(GL_ZERO, GL_ONE);
        break;
    case QPainter::CompositionMode_SourceIn:
        funcs.glBlendFunc(GL_DST_ALPHA, GL_ZERO);
        break;
    case QPainter::CompositionMode_DestinationIn:
        funcs.glBlendFunc(GL_ZERO, GL_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_SourceOut:
        funcs.glBlendFunc(GL_ONE_MINUS_DST_ALPHA, GL_ZERO);
        break;
    case QPainter::CompositionMode_DestinationOut:
        funcs.glBlendFunc(GL_ZERO, GL_ONE_MINUS_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_SourceAtop:
        funcs.glBlendFunc(GL_DST_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_DestinationAtop:
        funcs.glBlendFunc(GL_ONE_MINUS_DST_ALPHA, GL_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_Xor:
        funcs.glBlendFunc(GL_ONE_MINUS_DST_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        break;
    case QPainter::CompositionMode_Plus:
        funcs.glBlendFunc(GL_ONE, GL_ONE);
        break;
    case QPainter::CompositionMode_Multiply:
        funcs.glBlendEquation(GL_MULTIPLY_KHR);
        break;
    case QPainter::CompositionMode_Screen:
        funcs.glBlendEquation(GL_SCREEN_KHR);
        break;
    case QPainter::CompositionMode_Overlay:
        funcs.glBlendEquation(GL_OVERLAY_KHR);
        break;
    case QPainter::CompositionMode_Darken:
        funcs.glBlendEquation(GL_DARKEN_KHR);
        break;
    case QPainter::CompositionMode_Lighten:
        funcs.glBlendEquation(GL_LIGHTEN_KHR);
        break;
    case QPainter::CompositionMode_ColorDodge:
        funcs.glBlendEquation(GL_COLORDODGE_KHR);
        break;
    case QPainter::CompositionMode_ColorBurn:
        funcs.glBlendEquation(GL_COLORBURN_KHR);
        break;
    case QPainter::CompositionMode_HardLight:
        funcs.glBlendEquation(GL_HARDLIGHT_KHR);
        break;
    case QPainter::CompositionMode_SoftLight:
        funcs.glBlendEquation(GL_SOFTLIGHT_KHR);
        break;
    case QPainter::CompositionMode_Difference:
        funcs.glBlendEquation(GL_DIFFERENCE_KHR);
        break;
    case QPainter::CompositionMode_Exclusion:
        funcs.glBlendEquation(GL_EXCLUSION_KHR);
        break;
    default:
        qWarning("Unsupported composition mode");
        break;
    }

    compositionModeDirty = false;
}

//  from src/opengl/qopenglpaintengine.cpp, line 185, as _ZN28QOpenGL2PaintEngineExPrivate19activateTextureUnitEj
inline void QOpenGL2PaintEngineExPrivate::activateTextureUnit(GLenum textureUnit)
{
    if (textureUnit != lastTextureUnitUsed) {
        funcs.glActiveTexture(GL_TEXTURE0 + textureUnit);
        lastTextureUnitUsed = textureUnit;

        // We simplify things by keeping a single cached value of the last
        // texture that was bound, instead of one per texture unit. This
        // means that switching texture units could potentially mean we
        // need a re-bind and corresponding parameter updates.
        lastTextureUsed = GLuint(-1);
    }
}

//  from src/opengl/qopenglpaintengine.cpp, line 727, as _ZN28QOpenGL2PaintEngineExPrivate12resetGLStateEv
inline void QOpenGL2PaintEngineExPrivate::resetGLState()
{
    activateTextureUnit(QT_DEFAULT_TEXTURE_UNIT);

    funcs.glDisable(GL_BLEND);
    funcs.glDisable(GL_STENCIL_TEST);
    funcs.glDisable(GL_DEPTH_TEST);
    funcs.glDisable(GL_SCISSOR_TEST);
    funcs.glDepthMask(true);
    funcs.glDepthFunc(GL_LESS);
    funcs.glClearDepthf(1);
    funcs.glStencilMask(0xff);
    funcs.glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP);
    funcs.glStencilFunc(GL_ALWAYS, 0, 0xff);
    setVertexAttribArrayEnabled(QT_TEXTURE_COORDS_ATTR, false);
    setVertexAttribArrayEnabled(QT_VERTEX_COORDS_ATTR, false);
    setVertexAttribArrayEnabled(QT_OPACITY_ATTR, false);
    if (!QOpenGLContext::currentContext()->isOpenGLES()) {
        // gl_Color, corresponding to vertex attribute 3, may have been changed
        float color[] = { 1.0f, 1.0f, 1.0f, 1.0f };
        funcs.glVertexAttrib4fv(3, color);
    }
    if (vao.isCreated())
        vao.release();

    funcs.glBindBuffer(GL_ARRAY_BUFFER, 0);
    funcs.glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
}

//  from src/opengl/qopenglpaintengine.cpp, line 111, as _ZN28QOpenGL2PaintEngineExPrivate8setBrushERK6QBrush
inline void QOpenGL2PaintEngineExPrivate::setBrush(const QBrush& brush)
{
    if (qbrush_fast_equals(currentBrush, brush))
        return;

    const Qt::BrushStyle newStyle = qbrush_style(brush);
    Q_ASSERT(newStyle != Qt::NoBrush);

    currentBrush = brush;
    if (!currentBrushImage.isNull())
        currentBrushImage = QImage();
    brushUniformsDirty = true; // All brushes have at least one uniform

    if (newStyle > Qt::SolidPattern)
        brushTextureDirty = true;

    if (currentBrush.style() == Qt::TexturePattern
        && qHasPixmapTexture(brush) && brush.texture().isQBitmap())
    {
        shaderManager->setSrcPixelType(QOpenGLEngineShaderManager::TextureSrcWithPattern);
    } else {
        shaderManager->setSrcPixelType(newStyle);
    }
    shaderManager->optimiseForBrushTransform(currentBrush.transform().type());
}

//  from src/opengl/qopenglpaintengine.cpp, line 774, as _ZN28QOpenGL2PaintEngineExPrivate12transferModeE10EngineMode
inline void QOpenGL2PaintEngineExPrivate::transferMode(EngineMode newMode)
{
    if (newMode == mode)
        return;

    if (newMode == TextDrawingMode) {
        shaderManager->setHasComplexGeometry(true);
    } else {
        shaderManager->setHasComplexGeometry(false);
    }

    if (newMode == ImageDrawingMode) {
        uploadData(QT_VERTEX_COORDS_ATTR, staticVertexCoordinateArray, 8);
        uploadData(QT_TEXTURE_COORDS_ATTR, staticTextureCoordinateArray, 8);
    }

    if (newMode == ImageArrayDrawingMode || newMode == ImageOpacityArrayDrawingMode) {
        uploadData(QT_VERTEX_COORDS_ATTR, (GLfloat*)vertexCoordinateArray.data(), vertexCoordinateArray.vertexCount() * 2);
        uploadData(QT_TEXTURE_COORDS_ATTR, (GLfloat*)textureCoordinateArray.data(), textureCoordinateArray.vertexCount() * 2);

        if (newMode == ImageOpacityArrayDrawingMode)
            uploadData(QT_OPACITY_ATTR, (GLfloat*)opacityArray.data(), opacityArray.size());
    }

    // This needs to change when we implement high-quality anti-aliasing...
    if (newMode != TextDrawingMode)
        shaderManager->setMaskType(QOpenGLEngineShaderManager::NoMask);

    mode = newMode;
}

//  from src/opengl/qopenglpaintengine.cpp, line 138, as _ZN28QOpenGL2PaintEngineExPrivate15useSimpleShaderEv
inline void QOpenGL2PaintEngineExPrivate::useSimpleShader()
{
    shaderManager->useSimpleProgram();

    if (matrixDirty)
        updateMatrix();
}

//  from src/opengl/qopenglpaintengine.cpp, line 2427, as _ZN28QOpenGL2PaintEngineExPrivate9clearClipEj
inline void QOpenGL2PaintEngineExPrivate::clearClip(uint value)
{
    dirtyStencilRegion -= currentScissorBounds;

    funcs.glStencilMask(0xff);
    funcs.glClearStencil(value);
    funcs.glClear(GL_STENCIL_BUFFER_BIT);
    funcs.glStencilMask(0x0);

    q->state()->needsClipBufferClear = false;
}

//  from src/opengl/qopenglpaintengine.cpp, line 2360, as _ZN28QOpenGL2PaintEngineExPrivate21updateClipScissorTestEv
inline void QOpenGL2PaintEngineExPrivate::updateClipScissorTest()
{
    Q_Q(QOpenGL2PaintEngineEx);
    if (q->state()->clipTestEnabled) {
#ifndef QT_NO_DEBUG
        if (ctx->format().stencilBufferSize() <= 0)
            qWarning("OpenGL paint engine: attempted to use stencil test for clipping without requesting a stencil buffer.");
#endif
        funcs.glEnable(GL_STENCIL_TEST);
        funcs.glStencilFunc(GL_LEQUAL, q->state()->currentClip, ~GL_STENCIL_HIGH_BIT);
    } else {
        funcs.glDisable(GL_STENCIL_TEST);
        funcs.glStencilFunc(GL_ALWAYS, 0, 0xff);
    }

#ifdef QT_GL_NO_SCISSOR_TEST
    currentScissorBounds = QRect(0, 0, width, height);
#else
    QRect bounds = q->state()->rectangleClip;
    if (!q->state()->clipEnabled) {
        if (useSystemClip)
            bounds = systemClip.boundingRect();
        else
            bounds = QRect(0, 0, width, height);
    } else {
        if (useSystemClip)
            bounds = bounds.intersected(systemClip.boundingRect());
        else
            bounds = bounds.intersected(QRect(0, 0, width, height));
    }

    currentScissorBounds = bounds;

    if (bounds == QRect(0, 0, width, height)) {
        funcs.glDisable(GL_SCISSOR_TEST);
    } else {
        funcs.glEnable(GL_SCISSOR_TEST);
        setScissor(bounds);
    }
#endif
}

//  from src/opengl/qopenglpaintengine.cpp, line 2402, as _ZN28QOpenGL2PaintEngineExPrivate10setScissorERK5QRect
inline void QOpenGL2PaintEngineExPrivate::setScissor(const QRect &rect)
{
    const int left = rect.left();
    const int width = rect.width();
    int bottom = height - (rect.top() + rect.height());
    if (device->paintFlipped()) {
        bottom = rect.top();
    }
    const int height = rect.height();

    funcs.glScissor(left, bottom, width, height);
}

//  from src/opengl/qopenglpaintengine.cpp, line 2575, as _ZN28QOpenGL2PaintEngineExPrivate14regenerateClipEv
inline void QOpenGL2PaintEngineExPrivate::regenerateClip()
{
    systemStateChanged();
    replayClipOperations();
}

//  from src/opengl/qopenglpaintengine.cpp, line 2581, as _ZN28QOpenGL2PaintEngineExPrivate18systemStateChangedEv
inline void QOpenGL2PaintEngineExPrivate::systemStateChanged()
{
    Q_Q(QOpenGL2PaintEngineEx);

    q->state()->clipChanged = true;

    if (systemClip.isEmpty()) {
        useSystemClip = false;
    } else {
        if (q->paintDevice()->devType() == QInternal::Widget && currentClipDevice) {
            //QWidgetPrivate *widgetPrivate = qt_widget_private(static_cast<QWidget *>(currentClipDevice)->window());
            //useSystemClip = widgetPrivate->extra && widgetPrivate->extra->inRenderWithPainter;
            useSystemClip = true;
        } else {
            useSystemClip = true;
        }
    }

    q->state()->clipTestEnabled = false;
    q->state()->needsClipBufferClear = true;

    q->state()->currentClip = 1;
    maxClip = 1;

    q->state()->rectangleClip = useSystemClip ? systemClip.boundingRect() : QRect(0, 0, width, height);
    updateClipScissorTest();

    if (systemClip.rectCount() == 1) {
        if (systemClip.boundingRect() == QRect(0, 0, width, height))
            useSystemClip = false;
#ifndef QT_GL_NO_SCISSOR_TEST
        // scissoring takes care of the system clip
        return;
#endif
    }

    if (useSystemClip) {
        clearClip(0);

        QPainterPath path;
        path.addRegion(systemClip);

        q->state()->currentClip = 0;
        writeClip(qtVectorPathForPath(q->state()->matrix.inverted().map(path)), 1);
        q->state()->currentClip = 1;
        q->state()->clipTestEnabled = true;
    }
}

//  from src/opengl/qopenglpaintengine.cpp, line 2716, as _ZN28QOpenGL2PaintEngineExPrivate27setVertexAttribArrayEnabledEib
inline void QOpenGL2PaintEngineExPrivate::setVertexAttribArrayEnabled(int arrayIndex, bool enabled)
{
    Q_ASSERT(arrayIndex < QT_GL_VERTEX_ARRAY_TRACKED_COUNT);

    if (vertexAttributeArraysEnabledState[arrayIndex] && !enabled)
        funcs.glDisableVertexAttribArray(arrayIndex);

    if (!vertexAttributeArraysEnabledState[arrayIndex] && enabled)
        funcs.glEnableVertexAttribArray(arrayIndex);

    vertexAttributeArraysEnabledState[arrayIndex] = enabled;
}

//  from src/opengl/qopenglpaintengine.cpp, line 2729, as _ZN28QOpenGL2PaintEngineExPrivate11syncGlStateEv
inline void QOpenGL2PaintEngineExPrivate::syncGlState()
{
    for (int i = 0; i < QT_GL_VERTEX_ARRAY_TRACKED_COUNT; ++i) {
        if (vertexAttributeArraysEnabledState[i])
            funcs.glEnableVertexAttribArray(i);
        else
            funcs.glDisableVertexAttribArray(i);
    }
}
//  -----------------------------------------------------------------------

//  A QOpenGL2PaintEngineExPrivate that Python can take functions over in. Every QOpenGL2PaintEngineExPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpenGL2PaintEngineExPrivateCall0)(const void *, int *);
typedef void * (*CuteQOpenGL2PaintEngineExPrivateCall1)(const void *, int *);
class CuteQOpenGL2PaintEngineExPrivate : public QOpenGL2PaintEngineExPrivate {
public:
  using QOpenGL2PaintEngineExPrivate::QOpenGL2PaintEngineExPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QOpenGL2PaintEngineExPrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExPrivateCall0 call = reinterpret_cast<CuteQOpenGL2PaintEngineExPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineExPrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExPrivateCall1 call = reinterpret_cast<CuteQOpenGL2PaintEngineExPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }
};

//  QOpenGL2PaintEngineEx *QOpenGL2PaintEngineExPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineEx *ritual_ZN28QOpenGL2PaintEngineExPrivate6q_funcEv(
    QOpenGL2PaintEngineExPrivate *self) {
  return self->q_func();
}

//  const QOpenGL2PaintEngineEx *QOpenGL2PaintEngineExPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpenGL2PaintEngineEx *ritual_ZNK28QOpenGL2PaintEngineExPrivate6q_funcEv(
    const QOpenGL2PaintEngineExPrivate *self) {
  return self->q_func();
}

//  QOpenGL2PaintEngineExPrivate::~QOpenGL2PaintEngineExPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivateD1Ev(
    QOpenGL2PaintEngineExPrivate *self) {
  delete self;
}

//  void QOpenGL2PaintEngineExPrivate::updateMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate12updateMatrixEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->updateMatrix();
}

//  void QOpenGL2PaintEngineExPrivate::updateCompositionMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate21updateCompositionModeEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->updateCompositionMode();
}

//  void QOpenGL2PaintEngineExPrivate::activateTextureUnit(GLenum
//      textureUnit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate19activateTextureUnitEj(
    QOpenGL2PaintEngineExPrivate *self,
    GLenum textureUnit) {
  self->activateTextureUnit(textureUnit);
}

//  void QOpenGL2PaintEngineExPrivate::resetGLState()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate12resetGLStateEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->resetGLState();
}

//  void QOpenGL2PaintEngineExPrivate::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate8setBrushERK6QBrush(
    QOpenGL2PaintEngineExPrivate *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  void QOpenGL2PaintEngineExPrivate::transferMode(EngineMode newMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate12transferModeE10EngineMode(
    QOpenGL2PaintEngineExPrivate *self,
    EngineMode newMode) {
  self->transferMode(newMode);
}

//  void QOpenGL2PaintEngineExPrivate::useSimpleShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate15useSimpleShaderEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->useSimpleShader();
}

//  void QOpenGL2PaintEngineExPrivate::clearClip(uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate9clearClipEj(
    QOpenGL2PaintEngineExPrivate *self,
    uint value) {
  self->clearClip(value);
}

//  void QOpenGL2PaintEngineExPrivate::updateClipScissorTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate21updateClipScissorTestEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->updateClipScissorTest();
}

//  void QOpenGL2PaintEngineExPrivate::setScissor(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate10setScissorERK5QRect(
    QOpenGL2PaintEngineExPrivate *self,
    const QRect *rect) {
  self->setScissor(*rect);
}

//  void QOpenGL2PaintEngineExPrivate::regenerateClip()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate14regenerateClipEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->regenerateClip();
}

//  void QOpenGL2PaintEngineExPrivate::systemStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate18systemStateChangedEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->systemStateChanged();
}

//  void QOpenGL2PaintEngineExPrivate::setVertexAttribArrayEnabled(int
//      arrayIndex, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate27setVertexAttribArrayEnabledEib(
    QOpenGL2PaintEngineExPrivate *self,
    int arrayIndex,
    bool enabled) {
  self->setVertexAttribArrayEnabled(arrayIndex, enabled);
}

//  void QOpenGL2PaintEngineExPrivate::syncGlState()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpenGL2PaintEngineExPrivate11syncGlStateEv(
    QOpenGL2PaintEngineExPrivate *self) {
  self->syncGlState();
}

//  QOpenGLEngineShaderManager *QOpenGL2PaintEngineExPrivate::shaderManagerFo
//      rEngine(QOpenGL2PaintEngineEx *engine)
extern "C" Q_DECL_EXPORT
QOpenGLEngineShaderManager *ritual_ZN28QOpenGL2PaintEngineExPrivate22shaderManagerForEngineEP21QOpenGL2PaintEngineEx(
    QOpenGL2PaintEngineEx *engine) {
  return QOpenGL2PaintEngineExPrivate::shaderManagerForEngine(engine);
}

//  QOpenGL2PaintEngineExPrivate
//      *QOpenGL2PaintEngineExPrivate::getData(QOpenGL2PaintEngineEx *engine)
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineExPrivate *ritual_ZN28QOpenGL2PaintEngineExPrivate7getDataEP21QOpenGL2PaintEngineEx(
    QOpenGL2PaintEngineEx *engine) {
  return QOpenGL2PaintEngineExPrivate::getData(engine);
}

//  a Python function taken by a CuteQOpenGL2PaintEngineExPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGL2PaintEngineExPrivate(
    QOpenGL2PaintEngineExPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGL2PaintEngineExPrivate *>(self)->take(key, call);
}
